"""
Keneviz VIP Panel - app.py (Güncellenmiş sürüm)
- reCAPTCHA v2 doğrulama
- Yeni API listesi
- /api/sorgu route'u (frontend için)
- Admin ve key yönetimi
- Worker proxy fonksiyonları
"""

from datetime import datetime, timedelta
import os
import secrets
import string
import urllib.parse
import requests
import time

from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for, jsonify)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'keneviz.sqlite')

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', secrets.token_urlsafe(32))

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'sistemnabide')
RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY', 'your_recaptcha_secret_key_here')

db = SQLAlchemy(app)

# ----------------------------------------------------------------------------
# Models
# ----------------------------------------------------------------------------
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False, index=True)
    plan = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, default=True)
    notes = db.Column(db.Text, nullable=True)

    def is_expired(self):
        if not self.expires_at:
            return False
        return datetime.utcnow() > self.expires_at

# ----------------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------------
def init_db():
    with app.app_context():
        db.create_all()
        if Admin.query.first() is None:
            admin_pw = ADMIN_PASSWORD
            admin = Admin(username='admin', password_hash=generate_password_hash(admin_pw))
            db.session.add(admin)
            db.session.commit()
            app.logger.info("[setup] created admin user 'admin'")


def generate_key_string(length=20):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

PLAN_TO_DAYS = {
    '1week': 7,
    '1month': 30,
    '3month': 90,
    '1year': 365,
    'free': None
}


def create_key(plan='1month', notes=None):
    while True:
        k = generate_key_string(20)
        if not Key.query.filter_by(key=k).first():
            break
    expires = None
    days = PLAN_TO_DAYS.get(plan)
    if days:
        expires = datetime.utcnow() + timedelta(days=days)
    key = Key(key=k, plan=plan, expires_at=expires, notes=notes)
    db.session.add(key)
    db.session.commit()
    return key


def verify_key_string(kstr):
    if not kstr:
        return None
    key = Key.query.filter_by(key=kstr, active=True).first()
    if not key:
        return None
    if key.is_expired():
        key.active = False
        db.session.commit()
        return None
    return key

# ----------------------------------------------------------------------------
# reCAPTCHA doğrulama
# ----------------------------------------------------------------------------
def verify_recaptcha(response_token):
    """reCAPTCHA v2 doğrulama"""
    try:
        data = {
            'secret': RECAPTCHA_SECRET_KEY,
            'response': response_token
        }
        resp = requests.post('https://www.google.com/recaptcha/api/siteverify',
                           data=data, timeout=10)
        result = resp.json()
        return result.get('success', False)
    except Exception as e:
        app.logger.error(f"reCAPTCHA doğrulama hatası: {e}")
        return False

# ----------------------------------------------------------------------------
# Yeni API listesi
# ----------------------------------------------------------------------------
APIS = [
    {"ad": "Seçmen Sorgulama", "url": "http://api.nabi.gt.tc/secmen?tc={tc}", "params": "tc"},
    {"ad": "Öğretmen Sorgulama", "url": "http://api.nabi.gt.tc/ogretmen?ad={ad}&soyad={soyad}", "params": "ad, soyad"},
    {"ad": "Yabancı Sorgulama", "url": "http://api.nabi.gt.tc/yabanci?ad={ad}&soyad={soyad}", "params": "ad, soyad"},
    {"ad": "Site Log Sorgulama", "url": "http://api.nabi.gt.tc/log?site={site}", "params": "site"},
    {"ad": "Vesika Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/vesika2?tc={tc}", "params": "tc"},
    {"ad": "Tapu Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/tapu2?tc={tc}", "params": "tc"},
    {"ad": "İş Kaydı Sorgulama", "url": "http://api.nabi.gt.tc/iskaydi?adsoyad={adsoyad}", "params": "adsoyad"},
    {"ad": "Sertifika Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/sertifika2?tc={tc}", "params": "tc"},
    {"ad": "Papara No Sorgulama", "url": "http://api.nabi.gt.tc/papara?paparano={paparano}", "params": "paparano"},
    {"ad": "İninal No Sorgulama", "url": "http://api.nabi.gt.tc/ininal?ininal_no={ininal_no}", "params": "ininal_no"},
    {"ad": "TurkNet Sorgulama", "url": "http://api.nabi.gt.tc/turknet?tc={tc}", "params": "tc"},
    {"ad": "Seri No Sorgulama", "url": "http://api.nabi.gt.tc/serino?tc={tc}", "params": "tc"},
    {"ad": "Firma Ünvan Sorgulama", "url": "http://api.nabi.gt.tc/firma?unvan={unvan}", "params": "unvan"},
    {"ad": "Craftrise Kullanıcı Sorgu", "url": "http://api.nabi.gt.tc/craftrise?ad={ad}", "params": "ad"},
    {"ad": "SGK Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/sgk2?tc={tc}", "params": "tc"},
    {"ad": "Plaka Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/plaka2?plaka={plaka}", "params": "plaka"},
    {"ad": "Plaka İsim Sorgulama", "url": "http://api.nabi.gt.tc/plakaismi?isim={isim}", "params": "isim"},
    {"ad": "Plaka Borç Sorgulama", "url": "http://api.nabi.gt.tc/plakaborc?plaka={plaka}", "params": "plaka"},
    {"ad": "AKP Üye Sorgulama", "url": "http://api.nabi.gt.tc/akp?ad={ad}&soyad={soyad}", "params": "ad, soyad"},
    {"ad": "AI Fotoğraf Üretici", "url": "http://api.nabi.gt.tc/aifoto?img={img}", "params": "img"},
    {"ad": "Instagram Kullanıcı Sorgulama", "url": "http://api.nabi.gt.tc/insta?usr={usr}", "params": "usr"},
    {"ad": "Facebook Kullanıcı Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/facebook_hanedan?ad={ad}&soyad={soyad}", "params": "ad, soyad"},
    {"ad": "Üniversite Öğrenci Sorgulama", "url": "http://api.nabi.gt.tc/uni?tc={tc}", "params": "tc"},
    {"ad": "LGS Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/lgs_hanedan?tc={tc}", "params": "tc"},
    {"ad": "Okul Numarası Sorgulama", "url": "http://api.nabi.gt.tc/okulno_hanedan?tc={tc}", "params": "tc"},
    {"ad": "TC Sorgulama", "url": "http://api.nabi.gt.tc/tc_sorgulama?tc={tc}", "params": "tc"},
    {"ad": "TC PRO Sorgulama", "url": "http://api.nabi.gt.tc/tc_pro_sorgulama?tc={tc}", "params": "tc"},
    {"ad": "Hayat Hikayesi Sorgulama", "url": "http://api.nabi.gt.tc/hayat_hikayesi?tc={tc}", "params": "tc"},
    {"ad": "Ad Soyad Sorgulama", "url": "http://api.nabi.gt.tc/ad_soyad?ad={ad}&soyad={soyad}", "params": "ad, soyad"},
    {"ad": "Ad Soyad PRO Sorgulama", "url": "http://api.nabi.gt.tc/ad_soyad_pro?tc={tc}", "params": "tc"},
    {"ad": "İş Yeri Sorgulama", "url": "http://api.nabi.gt.tc/is_yeri?tc={tc}", "params": "tc"},
    {"ad": "Vergi No Sorgulama", "url": "http://api.nabi.gt.tc/vergi_no?vergi={vergi}", "params": "vergi"},
    {"ad": "Yaş Sorgulama", "url": "http://api.nabi.gt.tc/yas?tc={tc}", "params": "tc"},
    {"ad": "TC GSM Sorgulama", "url": "http://api.nabi.gt.tc/tc_gsm?tc={tc}", "params": "tc"},
    {"ad": "GSM TC Sorgulama", "url": "http://api.nabi.gt.tc/gsm_tc?gsm={gsm}", "params": "gsm"},
    {"ad": "Adres Sorgulama", "url": "http://api.nabi.gt.tc/adres?tc={tc}", "params": "tc"},
    {"ad": "Hane Sorgulama", "url": "http://api.nabi.gt.tc/hane?tc={tc}", "params": "tc"},
    {"ad": "Apartman Sorgulama", "url": "http://api.nabi.gt.tc/apartman?tc={tc}", "params": "tc"},
    {"ad": "Ada Parsel Sorgulama", "url": "http://api.nabi.gt.tc/ada_parsel?il={il}&ada={ada}&parsel={parsel}", "params": "il, ada, parsel"},
    {"ad": "Adı İl İlçe Sorgulama", "url": "http://api.nabi.gt.tc/adi_il_ilce?ad={ad}&il={il}", "params": "ad, il"},
    {"ad": "Aile Sorgulama", "url": "http://api.nabi.gt.tc/aile?tc={tc}", "params": "tc"},
    {"ad": "Aile PRO Sorgulama", "url": "http://api.nabi.gt.tc/aile_pro?tc={tc}", "params": "tc"},
    {"ad": "Eş Sorgulama", "url": "http://api.nabi.gt.tc/es?tc={tc}", "params": "tc"},
    {"ad": "Sülale Sorgulama", "url": "http://api.nabi.gt.tc/sulale?tc={tc}", "params": "tc"},
    {"ad": "LGS Sorgulama", "url": "http://api.nabi.gt.tc/lgs?tc={tc}", "params": "tc"},
    {"ad": "E-Kurs Sorgulama", "url": "http://api.nabi.gt.tc/e_kurs?tc={tc}&okulno={okulno}", "params": "tc, okulno"},
    {"ad": "IP Sorgulama", "url": "http://api.nabi.gt.tc/ip?domain={domain}", "params": "domain"},
    {"ad": "DNS Sorgulama", "url": "http://api.nabi.gt.tc/dns?domain={domain}", "params": "domain"},
    {"ad": "Whois Sorgulama", "url": "http://api.nabi.gt.tc/whois?domain={domain}", "params": "domain"},
    {"ad": "Subdomain Sorgulama", "url": "http://api.nabi.gt.tc/subdomain?url={url}", "params": "url"},
    {"ad": "Leak Sorgulama", "url": "http://api.nabi.gt.tc/leak?query={query}", "params": "query"},
    {"ad": "Telegram Sorgulama", "url": "http://api.nabi.gt.tc/telegram?kullanici={kullanici}", "params": "kullanici"},
    {"ad": "Şifre Encrypt", "url": "http://api.nabi.gt.tc/sifre_encrypt?method={method}&password={password}", "params": "method, password"}
]

# API parametreleri için mapping
API_PARAMS = {}
for api in APIS:
    api_name = api['ad'].lower().replace(' ', '_').replace('(', '').replace(')', '')
    params_str = api.get('params', '')
    if params_str:
        params_list = [p.strip() for p in params_str.split(',')]
        API_PARAMS[api_name] = params_list
    else:
        API_PARAMS[api_name] = []

# Worker URL çözümleme
def resolve_worker_url(api_name, params):
    """API ismine göre URL oluştur"""
    # API ismini normalize et
    normalized_name = api_name.lower().replace(' ', '_').replace('(', '').replace(')', '')

    # API'yi bul
    target_api = None
    for api in APIS:
        if api['ad'].lower().replace(' ', '_').replace('(', '').replace(')', '') == normalized_name:
            target_api = api
            break

    if not target_api:
        return None

    # URL'yi parametrelerle doldur
    url_template = target_api['url']
    try:
        formatted_url = url_template.format(**params)
        return formatted_url
    except KeyError as e:
        app.logger.error(f"Eksik parametre: {e} için {api_name}")
        return None

def proxy_worker_request(url):
    try:
        resp = requests.get(url, timeout=10)
        status = resp.status_code
        ctype = resp.headers.get('Content-Type','').lower()
        if 'application/json' in ctype or resp.text.strip().startswith('{') or resp.text.strip().startswith('['):
            try:
                return True, resp.json(), status
            except Exception:
                return True, resp.text, status
        else:
            return True, resp.text, status
    except requests.RequestException as e:
        return False, str(e), 502

# ----------------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------------

@app.route('/')
def index():
    if session.get('key_id'):
        return redirect(url_for('panel'))
    if not session.get('recaptcha_verified'):
        return redirect(url_for('robot_dogrulama') + '?next=/login')
    return render_template('index.html')


@app.route('/robot_dogrulama')
def robot_dogrulama():
    return render_template('robot_dogrulama.html')


@app.route('/verify_recaptcha', methods=['POST'])
def verify_recaptcha_route():
    """reCAPTCHA doğrulama endpoint'i"""
    data = request.get_json() or {}
    recaptcha_token = data.get('recaptcha_token')

    if not recaptcha_token:
        return jsonify({'success': False, 'error': 'reCAPTCHA token eksik'}), 400

    if verify_recaptcha(recaptcha_token):
        session['recaptcha_verified'] = True
        next_url = request.args.get('next', '/login')
        app.logger.info("reCAPTCHA doğrulama başarılı")
        return jsonify({'success': True, 'redirect': next_url})
    else:
        app.logger.warning("reCAPTCHA doğrulama başarısız")
        return jsonify({'success': False, 'error': 'reCAPTCHA doğrulama başarısız'}), 403


@app.route('/sorgu.html')
def sorgu_page():
    return render_template('sorgu.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('recaptcha_verified'):
        return redirect(url_for('robot_dogrulama') + '?next=/login')
    if request.method == 'GET':
        return render_template('login.html')
    key_str = request.form.get('key', '').strip()
    key = verify_key_string(key_str)
    if not key:
        flash('Geçersiz veya süresi dolmuş key')
        return redirect(url_for('login'))
    session['key_id'] = key.id
    session.pop('recaptcha_verified', None)
    return redirect(url_for('panel'))


@app.route('/logout')
def logout():
    session.pop('key_id', None)
    session.pop('admin_id', None)
    session.pop('recaptcha_verified', None)
    return redirect(url_for('index'))


@app.route('/panel')
def panel():
    kid = session.get('key_id')
    if not kid:
        return redirect(url_for('login'))
    key = Key.query.filter_by(id=kid).first()
    if not key or not key.active or key.is_expired():
        session.pop('key_id', None)
        flash('Key geçersiz veya süresi dolmuş')
        return redirect(url_for('login'))
    remaining = 'Limitsiz'
    if key.expires_at:
        remaining_delta = key.expires_at - datetime.utcnow()
        remaining = f"{remaining_delta.days} gün {remaining_delta.seconds//3600} saat"
    return render_template('panel.html', key=key, apis=APIS, remaining=remaining)

# ----------------------------------------------------------------------------
# Admin routes
# ----------------------------------------------------------------------------

@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin_login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    admin = Admin.query.filter_by(username=username).first()
    if not admin or not admin.check_password(password):
        flash('Geçersiz admin bilgileri')
        return redirect(url_for('admin_login'))
    session['admin_id'] = admin.id
    return redirect(url_for('admin_panel'))


@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    return redirect(url_for('admin_login'))


@app.route('/admin')
def admin_panel():
    admin_id = session.get('admin_id')
    if not admin_id:
        return redirect(url_for('admin_login'))
    keys = Key.query.order_by(Key.created_at.desc()).limit(200).all()
    return render_template('admin_panel.html', keys=keys)


@app.route('/admin/generate')
def admin_generate():
    admin_id = session.get('admin_id')
    if not admin_id:
        return redirect(url_for('admin_login'))
    plan = request.args.get('plan', '1month')
    try:
        qty = int(request.args.get('qty', '1'))
    except ValueError:
        qty = 1
    note = request.args.get('note', None)

    created = []
    for _ in range(max(1, min(qty, 1000))):
        k = create_key(plan=plan, notes=note)
        created.append(k)

    lines = []
    for k in created:
        lines.append(f"New key created: {k.key} (plan={k.plan})")
    return "<br>".join(lines)

# ----------------------------------------------------------------------------
# API endpoints
# ----------------------------------------------------------------------------

@app.route('/api/user')
def api_user():
    kid = session.get('key_id')
    if not kid:
        return jsonify({'logged_in': False, 'role': 'guest', 'username': None})
    key = Key.query.filter_by(id=kid).first()
    if not key or not key.active or key.is_expired():
        return jsonify({'logged_in': False, 'role': 'guest', 'username': None})
    role = 'vip' if key.plan != 'free' else 'free'
    username = f"user{key.id}"
    return jsonify({'logged_in': True, 'role': role, 'username': username})


@app.route('/api/sorgu', methods=['POST'])
def api_sorgu():
    # Oturum bazlı erişim (frontend panelden çağrılacak)
    kid = session.get('key_id')
    if not kid:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    key_obj = Key.query.filter_by(id=kid).first()
    if not key_obj or not key_obj.active or key_obj.is_expired():
        return jsonify({'success': False, 'error': 'Invalid or expired key'}), 401

    payload = request.get_json() or {}
    api_name = payload.get('api') or payload.get('action') or payload.get('slug')
    if not api_name:
        return jsonify({'success': False, 'error': 'Missing api name'}), 400

    params = {k:v for k,v in payload.items() if k not in ['api','action','slug'] and v is not None}

    url = resolve_worker_url(api_name, params)
    if not url:
        return jsonify({'success': False, 'error': 'Unable to resolve worker endpoint'}), 400

    ok, data, status = proxy_worker_request(url)
    if not ok:
        return jsonify({'success': False, 'error': 'Upstream request failed', 'detail': data}), status
    if isinstance(data, (dict, list)):
        return jsonify({'success': True, 'data': data}), status
    return jsonify({'success': True, 'data': data}), status


@app.route('/api/list')
def api_list():
    key_header = request.args.get('key') or request.headers.get('X-API-KEY')
    key_obj = verify_key_string(key_header) if key_header else None
    if not key_obj:
        return jsonify({'error':'Invalid or missing key'}), 401
    return jsonify({'apis': APIS, 'plan': key_obj.plan})

# ----------------------------------------------------------------------------
# Startup
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
