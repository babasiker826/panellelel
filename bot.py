"""
Keneviz VIP Panel - app.py (HTML uyumlu güncellenmiş sürüm)
- Her sorgu için özel HTML sayfaları
- Kırmızı 3D animasyon desteği
- reCAPTCHA v2 doğrulama
- Yeni API listesi
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
# reCAPTCHA anahtarları
RECAPTCHA_SITE_KEY = '6Lc-U90rAAAAAL6lqeyBZf9o7EW1e2sUBEKhAlAG'
RECAPTCHA_SECRET_KEY = '6Lc-U90rAAAAAMkzZR_RRwPGhGAOaiefasMYwwqc'

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
# Yeni API listesi (HTML'deki menüyle uyumlu)
# ----------------------------------------------------------------------------
APIS = [
    {"ad": "Ad Soyad Sorgulama", "url": "http://api.nabi.gt.tc/ad_soyad?ad={ad}&soyad={soyad}", "params": "ad, soyad", "html": "adsoyad.html"},
    {"ad": "TC Sorgulama", "url": "http://api.nabi.gt.tc/tc_sorgulama?tc={tc}", "params": "tc", "html": "tc.html"},
    {"ad": "Telegram Sorgulama", "url": "http://api.nabi.gt.tc/telegram?kullanici={kullanici}", "params": "kullanici", "html": "telegram.html"},
    {"ad": "IP Sorgulama", "url": "http://api.nabi.gt.tc/ip?domain={domain}", "params": "domain", "html": "ip.html"},
    {"ad": "DNS Sorgulama", "url": "http://api.nabi.gt.tc/dns?domain={domain}", "params": "domain", "html": "dns.html"},
    {"ad": "Whois Sorgulama", "url": "http://api.nabi.gt.tc/whois?domain={domain}", "params": "domain", "html": "whois.html"},
    {"ad": "Şifre Encrypt", "url": "http://api.nabi.gt.tc/sifre_encrypt?method={method}&password={password}", "params": "method, password", "html": "sifre-encrypt.html"},
    {"ad": "Subdomain Sorgulama", "url": "http://api.nabi.gt.tc/subdomain?url={url}", "params": "url", "html": "subdomain.html"},
    {"ad": "Hava Durumu", "url": "http://api.nabi.gt.tc/hava_durumu?sehir={sehir}", "params": "sehir", "html": "hava-durumu.html"},
    {"ad": "E-Kurs Sorgulama", "url": "http://api.nabi.gt.tc/e_kurs?tc={tc}&okulno={okulno}", "params": "tc, okulno", "html": "e-kurs.html"},
    {"ad": "TC PRO Sorgulama", "url": "http://api.nabi.gt.tc/tc_pro_sorgulama?tc={tc}", "params": "tc", "html": "tc-pro.html"},
    {"ad": "Ehliyet Sorgulama", "url": "http://api.nabi.gt.tc/ehliyet?tc={tc}", "params": "tc", "html": "ehliyet.html"},
    {"ad": "IP Sorgulama", "url": "http://api.nabi.gt.tc/ip_premium?domain={domain}", "params": "domain", "html": "ip-premium.html"},
    {"ad": "Ada Parsel Sorgulama", "url": "http://api.nabi.gt.tc/ada_parsel?il={il}&ada={ada}&parsel={parsel}", "params": "il, ada, parsel", "html": "ada-parsel.html"},
    {"ad": "Sertifika Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/sertifika2?tc={tc}", "params": "tc", "html": "sertifika.html"},
    {"ad": "Vergi Levhası Sorgulama", "url": "http://api.nabi.gt.tc/vergi_levhasi?tc={tc}", "params": "tc", "html": "vergi-levhasi.html"},
    {"ad": "Facebook Kullanıcı Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/facebook_hanedan?ad={ad}&soyad={soyad}", "params": "ad, soyad", "html": "facebook.html"},
    {"ad": "Diploma Sorgulama", "url": "http://api.nabi.gt.tc/diploma?tc={tc}", "params": "tc", "html": "diploma.html"},
    {"ad": "İnternet Sorgulama", "url": "http://api.nabi.gt.tc/internet?tc={tc}", "params": "tc", "html": "internet.html"},
    {"ad": "Interpol Sorgulama", "url": "http://api.nabi.gt.tc/interpol?tc={tc}", "params": "tc", "html": "interpol.html"},
    {"ad": "Şehit Sorgulama", "url": "http://api.nabi.gt.tc/sehit?tc={tc}", "params": "tc", "html": "sehit.html"},
    {"ad": "GSM TC Sorgulama", "url": "http://api.nabi.gt.tc/gsm_tc?gsm={gsm}", "params": "gsm", "html": "gsm-tc.html"},
    {"ad": "TC GSM Sorgulama", "url": "http://api.nabi.gt.tc/tc_gsm?tc={tc}", "params": "tc", "html": "tc-gsm.html"},
    {"ad": "Operatör Sorgulama", "url": "http://api.nabi.gt.tc/operator?gsm={gsm}", "params": "gsm", "html": "operator.html"},
    {"ad": "Aile Sorgulama", "url": "http://api.nabi.gt.tc/aile?tc={tc}", "params": "tc", "html": "aile.html"},
    {"ad": "Aile PRO Sorgulama", "url": "http://api.nabi.gt.tc/aile_pro?tc={tc}", "params": "tc", "html": "aile-pro.html"},
    {"ad": "Eş Sorgulama", "url": "http://api.nabi.gt.tc/es?tc={tc}", "params": "tc", "html": "es.html"},
    {"ad": "Sülale Sorgulama", "url": "http://api.nabi.gt.tc/sulale?tc={tc}", "params": "tc", "html": "sulale.html"},
    {"ad": "LGS Sorgulama", "url": "http://api.nabi.gt.tc/lgs?tc={tc}", "params": "tc", "html": "lgs.html"},
    {"ad": "LGS Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/lgs_hanedan?tc={tc}", "params": "tc", "html": "lgs-hanedan.html"},
    {"ad": "Üniversite Öğrenci Sorgulama", "url": "http://api.nabi.gt.tc/uni?tc={tc}", "params": "tc", "html": "universite.html"},
    {"ad": "Okul Numarası Sorgulama", "url": "http://api.nabi.gt.tc/okulno_hanedan?tc={tc}", "params": "tc", "html": "okul-no.html"},
    {"ad": "Vergi No Sorgulama", "url": "http://api.nabi.gt.tc/vergi_no?vergi={vergi}", "params": "vergi", "html": "vergi-no.html"},
    {"ad": "Firma Ünvan Sorgulama", "url": "http://api.nabi.gt.tc/firma?unvan={unvan}", "params": "unvan", "html": "firma.html"},
    {"ad": "SGK Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/sgk2?tc={tc}", "params": "tc", "html": "sgk.html"},
    {"ad": "Seçmen Sorgulama", "url": "http://api.nabi.gt.tc/secmen?tc={tc}", "params": "tc", "html": "secmen.html"},
    {"ad": "Öğretmen Sorgulama", "url": "http://api.nabi.gt.tc/ogretmen?ad={ad}&soyad={soyad}", "params": "ad, soyad", "html": "ogretmen.html"},
    {"ad": "Yabancı Sorgulama", "url": "http://api.nabi.gt.tc/yabanci?ad={ad}&soyad={soyad}", "params": "ad, soyad", "html": "yabanci.html"},
    {"ad": "Site Log Sorgulama", "url": "http://api.nabi.gt.tc/log?site={site}", "params": "site", "html": "site-log.html"},
    {"ad": "Vesika Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/vesika2?tc={tc}", "params": "tc", "html": "vesika.html"},
    {"ad": "Tapu Sorgulama (Hanedan)", "url": "http://api.nabi.gt.tc/tapu2?tc={tc}", "params": "tc", "html": "tapu.html"}
]

# HTML sayfaları için route mapping
HTML_ROUTES = {
    'adsoyad.html': 'Ad Soyad Sorgulama',
    'tc.html': 'TC Sorgulama',
    'telegram.html': 'Telegram Sorgulama',
    'ip.html': 'IP Sorgulama',
    'dns.html': 'DNS Sorgulama',
    'whois.html': 'Whois Sorgulama',
    'sifre-encrypt.html': 'Şifre Encrypt',
    'subdomain.html': 'Subdomain Sorgulama',
    'hava-durumu.html': 'Hava Durumu',
    'e-kurs.html': 'E-Kurs Sorgulama',
    'tc-pro.html': 'TC PRO Sorgulama',
    'ehliyet.html': 'Ehliyet Sorgulama',
    'ip-premium.html': 'IP Sorgulama',
    'ada-parsel.html': 'Ada Parsel Sorgulama',
    'sertifika.html': 'Sertifika Sorgulama (Hanedan)',
    'vergi-levhasi.html': 'Vergi Levhası Sorgulama',
    'facebook.html': 'Facebook Kullanıcı Sorgulama (Hanedan)',
    'diploma.html': 'Diploma Sorgulama',
    'internet.html': 'İnternet Sorgulama',
    'interpol.html': 'Interpol Sorgulama',
    'sehit.html': 'Şehit Sorgulama',
    'gsm-tc.html': 'GSM TC Sorgulama',
    'tc-gsm.html': 'TC GSM Sorgulama',
    'operator.html': 'Operatör Sorgulama',
    'aile.html': 'Aile Sorgulama',
    'aile-pro.html': 'Aile PRO Sorgulama',
    'es.html': 'Eş Sorgulama',
    'sulale.html': 'Sülale Sorgulama',
    'lgs.html': 'LGS Sorgulama',
    'lgs-hanedan.html': 'LGS Sorgulama (Hanedan)',
    'universite.html': 'Üniversite Öğrenci Sorgulama',
    'okul-no.html': 'Okul Numarası Sorgulama',
    'vergi-no.html': 'Vergi No Sorgulama',
    'firma.html': 'Firma Ünvan Sorgulama',
    'sgk.html': 'SGK Sorgulama (Hanedan)',
    'secmen.html': 'Seçmen Sorgulama',
    'ogretmen.html': 'Öğretmen Sorgulama',
    'yabanci.html': 'Yabancı Sorgulama',
    'site-log.html': 'Site Log Sorgulama',
    'vesika.html': 'Vesika Sorgulama (Hanedan)',
    'tapu.html': 'Tapu Sorgulama (Hanedan)'
}

# Worker URL çözümleme
def resolve_worker_url(api_name, params):
    """API ismine göre URL oluştur"""
    target_api = None
    for api in APIS:
        if api['ad'] == api_name:
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
    return render_template('index.html', recaptcha_site_key=RECAPTCHA_SITE_KEY)


@app.route('/robot_dogrulama')
def robot_dogrulama():
    return render_template('robot_dogrulama.html', recaptcha_site_key=RECAPTCHA_SITE_KEY)


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


# Her sorgu için özel HTML sayfaları
@app.route('/<html_file>')
def sorgu_html_pages(html_file):
    if html_file in HTML_ROUTES:
        api_name = HTML_ROUTES[html_file]
        # API bilgisini bul
        api_info = None
        for api in APIS:
            if api['ad'] == api_name:
                api_info = api
                break
        
        if api_info:
            return render_template('sorgu_template.html', 
                                 api_name=api_name,
                                 api_info=api_info,
                                 recaptcha_site_key=RECAPTCHA_SITE_KEY)
    
    # Eğer dosya bulunamazsa 404
    return "Sayfa bulunamadı", 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('recaptcha_verified'):
        return redirect(url_for('robot_dogrulama') + '?next=/login')
    if request.method == 'GET':
        return render_template('login.html', recaptcha_site_key=RECAPTCHA_SITE_KEY)
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
    return render_template('panel.html', key=key, apis=APIS, remaining=remaining, recaptcha_site_key=RECAPTCHA_SITE_KEY)

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
    api_name = payload.get('api')
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
