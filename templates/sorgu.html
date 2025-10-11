<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>NABI SYSTEM - Sorgu Paneli</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

        /* KIRMIZI 3D ANİMASYON */
        #red-animation-canvas {
            position: fixed;
            inset: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            display: block;
            pointer-events: none;
            opacity: 0.85;
            transition: opacity .6s ease;
            will-change: transform;
        }

        body {
            background: #151520;
            color: #c5c7d6;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow-x: hidden;
            min-height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            width: 100%;
            margin-top: 20px;
        }

        .welcome-text {
            font-size: 36px;
            font-weight: bold;
            color: #ff4dff;
            text-shadow:
                0 0 6px rgba(255, 77, 255, 0.95),
                0 0 14px rgba(255, 77, 255, 0.8),
                0 0 28px rgba(142, 45, 255, 0.6),
                0 6px 30px rgba(20, 0, 40, 0.45);
            text-align: center;
            line-height: 1.2;
            white-space: pre-line;
        }
        .welcome-wrap {
            position: relative;
            display: inline-block;
            padding: 12px 18px;
            border-radius: 12px;
            margin-bottom: 20px;
            z-index: 10;
        }
        .welcome-wrap .glass-box {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 12px;
            background: rgba(255,255,255,0.06);
            backdrop-filter: blur(8px) saturate(120%);
            -webkit-backdrop-filter: blur(8px) saturate(120%);
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 8px 20px rgba(2,6,23,0.45);
            z-index: -1;
            pointer-events: none;
        }

        .form-container {
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(12px) saturate(140%);
            -webkit-backdrop-filter: blur(12px) saturate(140%);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 18px 40px rgba(2,6,23,0.6);
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #e6f9ff;
        }

        .form-group input, .form-group select, .form-group textarea {
            width: 100%;
            padding: 12px 15px;
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: #fff;
            font-size: 16px;
            transition: all 0.3s;
            resize: vertical;
        }

        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none;
            border-color: #ff4dff;
            box-shadow: 0 0 0 2px rgba(255, 77, 255, 0.2);
        }

        .btn-sorgula {
            background: linear-gradient(180deg,#ff4d4d,#ff1a1a);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            margin-top: 10px;
        }

        .btn-sorgula:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(255, 0, 0, 0.3);
        }

        .btn-sorgula:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .btn-ai {
            background: linear-gradient(180deg,#4d79ff,#1a4dff);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            margin-top: 10px;
        }

        .btn-ai:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(26, 77, 255, 0.3);
        }

        .btn-instagram {
            background: linear-gradient(180deg,#E1306C,#C13584);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            margin-top: 10px;
        }

        .btn-instagram:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(193, 53, 132, 0.3);
        }

        .result-container {
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(12px) saturate(140%);
            -webkit-backdrop-filter: blur(12px) saturate(140%);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 18px 40px rgba(2,6,23,0.6);
        }

        .result-title {
            font-size: 24px;
            font-weight: bold;
            color: #ff4dff;
            margin-bottom: 20px;
            text-align: center;
        }

        .table-container {
            overflow-x: auto;
        }

        .result-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        .result-table th {
            background: rgba(255, 77, 255, 0.1);
            padding: 12px 15px;
            text-align: left;
            font-weight: 600;
            color: #ff4dff;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .result-table td {
            padding: 12px 15px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .result-table tr:hover {
            background: rgba(255,255,255,0.02);
        }

        .btn-copy {
            background: rgba(255,255,255,0.1);
            color: #fff;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
        }

        .btn-copy:hover {
            background: rgba(255,255,255,0.2);
        }

        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }

        .loading-spinner {
            border: 3px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top: 3px solid #ff4dff;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .error-message {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid rgba(255, 0, 0, 0.3);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            color: #ff6b6b;
        }

        .success-message {
            background: rgba(0, 255, 0, 0.1);
            border: 1px solid rgba(0, 255, 0, 0.3);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            color: #6bff6b;
        }

        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        .nav-btn {
            background: rgba(255,255,255,0.05);
            color: #e6f9ff;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            display: inline-block;
        }

        .nav-btn:hover {
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
        }

        .__vip_blob { position: fixed; border-radius: 50%; opacity: 0.09; filter: blur(18px); z-index: -1; pointer-events: none; }
        .__vip_blob.a { width:480px; height:480px; left:-140px; top:-100px; background:linear-gradient(90deg,#ff0000,#ff6b6b); animation:__vip_floatA 18s ease-in-out infinite; }
        .__vip_blob.b { width:320px; height:320px; right:-120px; bottom:-120px; background:linear-gradient(90deg,#ff4757,#ff3838); animation:__vip_floatB 20s ease-in-out infinite; }
        @keyframes __vip_floatA { 0%{transform:translate(0,0)}50%{transform:translate(18px,26px)}100%{transform:translate(0,0)} }
        @keyframes __vip_floatB { 0%{transform:translate(0,0)}50%{transform:translate(-18px,-26px)}100%{transform:translate(0,0)} }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .info-item {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 8px;
            padding: 15px;
        }

        .info-label {
            font-size: 12px;
            color: #ff4dff;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .info-value {
            font-size: 14px;
            color: #e6f9ff;
            word-break: break-all;
        }

        .dynamic-fields {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }

        /* AI Sohbet Stilleri */
        .ai-chat-container {
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(12px) saturate(140%);
            -webkit-backdrop-filter: blur(12px) saturate(140%);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 18px 40px rgba(2,6,23,0.6);
            max-height: 500px;
            overflow-y: auto;
        }

        .chat-message {
            margin-bottom: 15px;
            padding: 12px 16px;
            border-radius: 12px;
            max-width: 80%;
        }

        .user-message {
            background: rgba(77, 121, 255, 0.2);
            border: 1px solid rgba(77, 121, 255, 0.3);
            margin-left: auto;
        }

        .ai-message {
            background: rgba(255, 77, 255, 0.1);
            border: 1px solid rgba(255, 77, 255, 0.2);
            margin-right: auto;
        }

        .message-content {
            color: #e6f9ff;
            line-height: 1.4;
        }

        .chat-input-container {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .chat-input {
            flex: 1;
            padding: 12px 15px;
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: #fff;
            font-size: 16px;
        }

        .chat-send-btn {
            background: linear-gradient(180deg,#4d79ff,#1a4dff);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .chat-send-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(26, 77, 255, 0.3);
        }

        .instagram-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }

        .stat-item {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 8px;
            padding: 15px;
            text-align: center;
        }

        .stat-value {
            font-size: 24px;
            font-weight: bold;
            color: #ff4dff;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 12px;
            color: #9aa4b2;
        }

        .payment-form {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }

        .card-input-group {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 10px;
            margin-bottom: 15px;
        }

        /* AI Düşünme Animasyonu */
        .ai-thinking {
            display: none;
            align-items: center;
            gap: 10px;
            padding: 10px 15px;
            background: rgba(255, 77, 255, 0.1);
            border-radius: 12px;
            margin: 10px 0;
            border: 1px solid rgba(255, 77, 255, 0.2);
        }

        .thinking-text {
            color: #ff4dff;
            font-weight: 600;
            font-size: 14px;
        }

        .thinking-dots {
            display: flex;
            gap: 4px;
        }

        .thinking-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #ff4dff;
            animation: thinkingBounce 1.4s ease-in-out infinite both;
        }

        .thinking-dot:nth-child(1) { animation-delay: -0.32s; }
        .thinking-dot:nth-child(2) { animation-delay: -0.16s; }
        .thinking-dot:nth-child(3) { animation-delay: 0s; }

        @keyframes thinkingBounce {
            0%, 80%, 100% {
                transform: scale(0);
                opacity: 0.5;
            }
            40% {
                transform: scale(1);
                opacity: 1;
            }
        }

        /* AI Yazıyor Animasyonu */
        .ai-typing {
            display: none;
            align-items: center;
            gap: 10px;
            padding: 10px 15px;
            background: rgba(77, 121, 255, 0.1);
            border-radius: 12px;
            margin: 10px 0;
            border: 1px solid rgba(77, 121, 255, 0.2);
        }

        .typing-text {
            color: #4d79ff;
            font-weight: 600;
            font-size: 14px;
        }

        .typing-indicator {
            display: flex;
            gap: 3px;
        }

        .typing-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #4d79ff;
            animation: typingPulse 1.5s ease-in-out infinite both;
        }

        .typing-dot:nth-child(1) { animation-delay: 0s; }
        .typing-dot:nth-child(2) { animation-delay: 0.2s; }
        .typing-dot:nth-child(3) { animation-delay: 0.4s; }

        @keyframes typingPulse {
            0%, 60%, 100% {
                transform: translateY(0);
                opacity: 0.4;
            }
            30% {
                transform: translateY(-10px);
                opacity: 1;
            }
        }

        @media (max-width: 768px) {
            .card-input-group {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- KIRMIZI 3D ANİMASYON -->
    <canvas id="red-animation-canvas" aria-hidden="true"></canvas>

    <div class="__vip_blob a" aria-hidden="true"></div>
    <div class="__vip_blob b" aria-hidden="true"></div>

    <div class="container">
        <div class="welcome-wrap">
            <div class="glass-box" aria-hidden="true"></div>
            <div class="welcome-text" id="current-api-title">
                NABI SYSTEM🌱
                Sorgu Paneli
            </div>
        </div>

        <div class="form-container" id="main-form-container">
            <form id="sorgu-form">
                <div id="dynamic-fields" class="dynamic-fields">
                    <!-- Dinamik input alanları buraya eklenecek -->
                </div>
                
                <button type="submit" class="btn-sorgula" id="sorgula-btn">
                    <i class="fas fa-search"></i> Sorgula
                </button>
            </form>
        </div>

        <!-- AI Sohbet Konteyneri -->
        <div class="form-container" id="ai-chat-section" style="display: none;">
            <div class="welcome-text" style="font-size: 24px; margin-bottom: 20px;" id="ai-welcome-title">
                AI Asistan - Sohbete Hoş Geldin
            </div>
            
            <!-- AI Düşünme Animasyonu -->
            <div class="ai-thinking" id="ai-thinking">
                <div class="thinking-text">AI düşünüyor</div>
                <div class="thinking-dots">
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                </div>
            </div>

            <!-- AI Yazıyor Animasyonu -->
            <div class="ai-typing" id="ai-typing">
                <div class="typing-text">AI yazıyor</div>
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>

            <div class="ai-chat-container" id="ai-chat-messages">
                <div class="chat-message ai-message">
                    <div class="message-content">
                        Merhaba! Ben bir AI asistanım. Size nasıl yardımcı olabilirim?
                    </div>
                </div>
            </div>
            <div class="chat-input-container">
                <input type="text" class="chat-input" id="ai-chat-input" placeholder="Mesajınızı yazın...">
                <button class="chat-send-btn" id="ai-send-btn">
                    <i class="fas fa-paper-plane"></i> Gönder
                </button>
            </div>
        </div>

        <!-- Instagram İstatistik Konteyneri -->
        <div class="form-container" id="instagram-stats-section" style="display: none;">
            <div class="welcome-text" style="font-size: 24px; margin-bottom: 20px;">
                Instagram İstatistikleri
            </div>
            <div class="instagram-stats">
                <div class="stat-item">
                    <div class="stat-value" id="followers-count">0</div>
                    <div class="stat-label">Takipçi</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value" id="likes-count">0</div>
                    <div class="stat-label">Beğeni</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value" id="comments-count">0</div>
                    <div class="stat-label">Yorum</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value" id="engagement-rate">0%</div>
                    <div class="stat-label">Etkileşim Oranı</div>
                </div>
            </div>
        </div>

        <!-- Iyzico Ödeme Formu -->
        <div class="form-container" id="payment-section" style="display: none;">
            <div class="welcome-text" style="font-size: 24px; margin-bottom: 20px;">
                Iyzico Ödeme Sistemi
            </div>
            <div class="payment-form">
                <form id="payment-form">
                    <div class="card-input-group">
                        <div class="form-group">
                            <label for="cc">Kart Numarası</label>
                            <input type="text" id="cc" name="cc" placeholder="1234 5678 9012 3456" maxlength="19" required>
                        </div>
                        <div class="form-group">
                            <label for="ay">Ay</label>
                            <input type="number" id="ay" name="ay" placeholder="MM" min="1" max="12" required>
                        </div>
                        <div class="form-group">
                            <label for="yil">Yıl</label>
                            <input type="number" id="yil" name="yil" placeholder="YY" min="23" max="40" required>
                        </div>
                        <div class="form-group">
                            <label for="cvv">CVV</label>
                            <input type="text" id="cvv" name="cvv" placeholder="123" maxlength="3" required>
                        </div>
                    </div>
                    <button type="submit" class="btn-sorgula">
                        <i class="fas fa-credit-card"></i> Ödemeyi Tamamla
                    </button>
                </form>
            </div>
        </div>

        <div class="loading" id="loading">
            <div class="loading-spinner"></div>
            <div>Sorgulanıyor...</div>
        </div>

        <div id="result-section" style="display: none;">
            <div class="result-container">
                <div class="result-title" id="result-title">Sorgu Sonuçları</div>
                <div id="info-grid" class="info-grid" style="display: none;">
                    <!-- Grid bilgileri burada gösterilecek -->
                </div>
                <div class="table-container">
                    <table class="result-table" id="main-table">
                        <thead id="table-head">
                            <!-- Tablo başlıkları dinamik olarak eklenecek -->
                        </thead>
                        <tbody id="table-body">
                            <!-- Sorgu sonuçları burada gösterilecek -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="error-section" class="error-message" style="display: none;">
            <!-- Hata mesajları burada gösterilecek -->
        </div>

        <div class="nav-buttons">
            <a href="panel.html" class="nav-btn"><i class="fas fa-home"></i> Panele Dön</a>
            <a href="logout" class="nav-btn"><i class="fas fa-sign-out-alt"></i> Çıkış Yap</a>
        </div>
    </div>

    <script>
        // API listesi - Backend'den gelen API'lerle senkronize
        const APIS = [
            // TC ve Kişi Sorguları
            { name: "Ad Soyad Sorgulama", value: "Ad Soyad Sorgulama", params: ["ad", "soyad"] },
            { name: "TC Sorgulama", value: "TC Sorgulama", params: ["tc"] },
            { name: "TC PRO Sorgulama", value: "TC PRO Sorgulama", params: ["tc"] },
            { name: "Aile Sorgulama", value: "Aile Sorgulama", params: ["tc"] },
            { name: "Aile PRO Sorgulama", value: "Aile PRO Sorgulama", params: ["tc"] },
            { name: "Eş Sorgulama", value: "Eş Sorgulama", params: ["tc"] },
            { name: "Sülale Sorgulama", value: "Sülale Sorgulama", params: ["tc"] },
            { name: "Kardeş Sorgulama", value: "Kardeş Sorgulama", params: ["tc"] },
            { name: "Çocuk Sorgulama", value: "Çocuk Sorgulama", params: ["tc"] },
            { name: "Kuzen Sorgulama", value: "Kuzen Sorgulama", params: ["tc"] },
            { name: "Randevu Sorgulama", value: "Randevu Sorgulama", params: ["tc"] },
            { name: "Ayak Sorgulama", value: "Ayak Sorgulama", params: ["tc"] },
            { name: "PKK Aranan Sorgulama", value: "PKK Aranan Sorgulama", params: ["ad", "soyad"] },
            
            // GSM Sorguları
            { name: "GSM TC Sorgulama", value: "GSM TC Sorgulama", params: ["gsm"] },
            { name: "TC GSM Sorgulama", value: "TC GSM Sorgulama", params: ["tc"] },
            { name: "Operatör Sorgulama", value: "Operatör Sorgulama", params: ["gsm"] },
            
            // Eğitim Sorguları
            { name: "E-Kurs Sorgulama", value: "E-Kurs Sorgulama", params: ["tc", "okulno"] },
            { name: "LGS Sorgulama", value: "LGS Sorgulama", params: ["tc"] },
            { name: "LGS Sorgulama (Hanedan)", value: "LGS Sorgulama (Hanedan)", params: ["tc"] },
            { name: "Üniversite Öğrenci Sorgulama", value: "Üniversite Öğrenci Sorgulama", params: ["tc"] },
            { name: "Üniversite Sorgulama (Hanedan)", value: "Üniversite Sorgulama (Hanedan)", params: ["tc"] },
            { name: "Okul Numarası Sorgulama", value: "Okul Numarası Sorgulama", params: ["tc"] },
            { name: "Öğretmen Sorgulama", value: "Öğretmen Sorgulama", params: ["ad", "soyad"] },
            { name: "Diploma Sorgulama", value: "Diploma Sorgulama", params: ["tc"] },
            
            // Sosyal Medya Sorguları
            { name: "Telegram Sorgulama", value: "Telegram Sorgulama", params: ["kullanici"] },
            { name: "Facebook Kullanıcı Sorgulama (Hanedan)", value: "Facebook Kullanıcı Sorgulama (Hanedan)", params: ["ad", "soyad"] },
            { name: "Mail Sorgulama", value: "Mail Sorgulama", params: ["mail", "sayi"] },
            { name: "Sicil Sorgulama", value: "Sicil Sorgulama", params: ["ad", "soyad"] },
            
            // Belge Sorguları
            { name: "Ehliyet Sorgulama", value: "Ehliyet Sorgulama", params: ["tc"] },
            { name: "Sertifika Sorgulama (Hanedan)", value: "Sertifika Sorgulama (Hanedan)", params: ["tc"] },
            { name: "Vesika Sorgulama (Hanedan)", value: "Vesika Sorgulama (Hanedan)", params: ["tc"] },
            { name: "Tapu Sorgulama (Hanedan)", value: "Tapu Sorgulama (Hanedan)", params: ["tc"] },
            
            // Network Sorguları
            { name: "IP Sorgulama", value: "IP Sorgulama", params: ["domain"] },
            { name: "IP Sorgulama (Premium)", value: "IP Sorgulama (Premium)", params: ["domain"] },
            { name: "DNS Sorgulama", value: "DNS Sorgulama", params: ["domain"] },
            { name: "Whois Sorgulama", value: "Whois Sorgulama", params: ["domain"] },
            { name: "Subdomain Sorgulama", value: "Subdomain Sorgulama", params: ["url"] },
            
            // YENİ AI İşlemleri
            { name: "GPT-4 Mini AI", value: "GPT-4 Mini AI", params: ["message"], type: "ai" },
            { name: "Gemini 1.5 Pro AI", value: "Gemini 1.5 Pro AI", params: ["message"], type: "ai" },
            { name: "GPT-5 Model AI", value: "GPT-5 Model AI", params: ["message"], type: "ai" },
            { name: "DeepSeek AI", value: "DeepSeek AI", params: ["message"], type: "ai" },
            
            // YENİ Instagram İşlemleri
            { name: "Instagram Takipçi", value: "Instagram Takipçi", params: ["username", "miktar"], type: "instagram" },
            { name: "Instagram Beğeni", value: "Instagram Beğeni", params: ["username", "miktar"], type: "instagram" },
            { name: "Instagram Yorum", value: "Instagram Yorum", params: ["username", "miktar"], type: "instagram" },
            
            // YENİ Ödeme Sistemi
            { name: "Iyzico Ödeme Sistemi", value: "Iyzico Ödeme Sistemi", params: ["cc", "ay", "yil", "cvv"], type: "payment" },
            
            // YENİ Keneviz API'leri
            { name: "Eş Sorgulama (Keneviz)", value: "Eş Sorgulama (Keneviz)", params: ["tc"] },
            { name: "Sürücü Sorgulama", value: "Sürücü Sorgulama", params: ["tc"] },
            { name: "Hayat Hikayesi Sorgulama", value: "Hayat Hikayesi Sorgulama", params: ["tc"] },
            
            // YENİ Nabi API'leri
            { name: "Hava Durumu (Yeni)", value: "Hava Durumu (Yeni)", params: [], type: "nocommand" },
            { name: "Kur Sorgulama", value: "Kur Sorgulama", params: [], type: "nocommand" },
            { name: "Steam Kod", value: "Steam Kod", params: [], type: "nocommand" },
            { name: "VP Kod", value: "VP Kod", params: [], type: "nocommand" },
            { name: "Free Kod", value: "Free Kod", params: [], type: "nocommand" },
            { name: "Kalp Kod", value: "Kalp Kod", params: [], type: "nocommand" },
            { name: "Sigma Kod", value: "Sigma Kod", params: [], type: "nocommand" },
            { name: "Live Kod", value: "Live Kod", params: [], type: "nocommand" },
            { name: "Imposter Kod", value: "Imposter Kod", params: [], type: "nocommand" },
            { name: "Play Kod", value: "Play Kod", params: [], type: "nocommand" },
            { name: "UC Kod", value: "UC Kod", params: [], type: "nocommand" },
            { name: "Midas Buy", value: "Midas Buy", params: [], type: "nocommand" },
            { name: "Predunyam", value: "Predunyam", params: [], type: "nocommand" },
            { name: "SMS Onay", value: "SMS Onay", params: [], type: "nocommand" },
            { name: "Zara", value: "Zara", params: [], type: "nocommand" },
            { name: "Exxen", value: "Exxen", params: [], type: "nocommand" },
            { name: "BluTV", value: "BluTV", params: [], type: "nocommand" },
            { name: "Amazon", value: "Amazon", params: [], type: "nocommand" },
            { name: "Purna", value: "Purna", params: [], type: "nocommand" },
            { name: "MLBB Kod", value: "MLBB Kod", params: [], type: "nocommand" },
            { name: "Kazandırıyo", value: "Kazandırıyo", params: [], type: "nocommand" },
            { name: "Robux Kod", value: "Robux Kod", params: [], type: "nocommand" },
            { name: "Car Parking", value: "Car Parking", params: [], type: "nocommand" },
            { name: "Roblox", value: "Roblox", params: [], type: "nocommand" },
            { name: "Twitter", value: "Twitter", params: [], type: "nocommand" },
            { name: "Netflix", value: "Netflix", params: [], type: "nocommand" },
            { name: "PUBG", value: "PUBG", params: [], type: "nocommand" },
            { name: "Hepsiburada", value: "Hepsiburada", params: [], type: "nocommand" },
            { name: "Hotmail", value: "Hotmail", params: [], type: "nocommand" },
            { name: "Valorant", value: "Valorant", params: [], type: "nocommand" },
            { name: "Facebook", value: "Facebook", params: [], type: "nocommand" },
            { name: "Troy", value: "Troy", params: [], type: "nocommand" },
            
            // Diğer Sorgular
            { name: "Hava Durumu", value: "Hava Durumu", params: ["sehir"] },
            { name: "Şifre Encrypt", value: "Şifre Encrypt", params: ["method", "password"] },
            { name: "Ada Parsel Sorgulama", value: "Ada Parsel Sorgulama", params: ["il", "ada", "parsel"] },
            { name: "Vergi Levhası Sorgulama", value: "Vergi Levhası Sorgulama", params: ["tc"] },
            { name: "İnternet Sorgulama", value: "İnternet Sorgulama", params: ["tc"] },
            { name: "Interpol Sorgulama", value: "Interpol Sorgulama", params: ["tc"] },
            { name: "Şehit Sorgulama", value: "Şehit Sorgulama", params: ["tc"] },
            { name: "Vergi No Sorgulama", value: "Vergi No Sorgulama", params: ["vergi"] },
            { name: "Firma Ünvan Sorgulama", value: "Firma Ünvan Sorgulama", params: ["unvan"] },
            { name: "SGK Sorgulama (Hanedan)", value: "SGK Sorgulama (Hanedan)", params: ["tc"] },
            { name: "Seçmen Sorgulama", value: "Seçmen Sorgulama", params: ["tc"] },
            { name: "Seçmen Sorgulama (Hanedan)", value: "Seçmen Sorgulama (Hanedan)", params: ["tc"] },
            { name: "Yabancı Sorgulama", value: "Yabancı Sorgulama", params: ["ad", "soyad"] },
            { name: "Site Log Sorgulama", value: "Site Log Sorgulama", params: ["site"] }
        ];

        let currentApi = '';
        let aiChatHistory = [];
        let thinkingTimeout = null;
        let typingTimeout = null;

        // Sayfa yüklendiğinde
        document.addEventListener('DOMContentLoaded', function() {
            // URL parametrelerini kontrol et
            const urlParams = new URLSearchParams(window.location.search);
            const apiFromUrl = urlParams.get('api');
            
            if (apiFromUrl) {
                currentApi = apiFromUrl;
                const selectedApi = APIS.find(api => api.value === currentApi);
                
                if (selectedApi) {
                    // Başlık güncelle
                    document.getElementById('current-api-title').innerHTML = `NABI SYSTEM🌱<br>${selectedApi.name}`;
                    
                    // Özel arayüz kontrolü
                    if (selectedApi.type === 'ai') {
                        showAIChatInterface(selectedApi);
                    } else if (selectedApi.type === 'instagram') {
                        showInstagramInterface(selectedApi);
                    } else if (selectedApi.type === 'payment') {
                        showPaymentInterface(selectedApi);
                    } else if (selectedApi.type === 'nocommand') {
                        showNoCommandInterface(selectedApi);
                    } else {
                        showStandardInterface(selectedApi);
                    }
                } else {
                    showError('Geçersiz sorgu türü!');
                }
            } else {
                showError('Sorgu türü belirtilmemiş!');
            }

            // Session kontrolü
            fetch('/api/user')
                .then(response => response.json())
                .then(user => {
                    if (!user.logged_in) {
                        window.location.href = '/login';
                    }
                })
                .catch(error => {
                    console.error('Kullanıcı kontrol hatası:', error);
                    window.location.href = '/login';
                });

            // AI sohbet event listener
            document.getElementById('ai-send-btn').addEventListener('click', sendAIMessage);
            document.getElementById('ai-chat-input').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendAIMessage();
                }
            });

            // Ödeme formu event listener
            document.getElementById('payment-form').addEventListener('submit', processPayment);
        });

        // Standart arayüz göster
        function showStandardInterface(api) {
            updateDynamicFields(api);
            document.getElementById('main-form-container').style.display = 'block';
        }

        // AI sohbet arayüzü göster
        function showAIChatInterface(api) {
            document.getElementById('main-form-container').style.display = 'none';
            document.getElementById('ai-chat-section').style.display = 'block';
            document.getElementById('ai-welcome-title').textContent = `${api.name} - Sohbete Hoş Geldin`;
            
            // Butonu AI moduna çevir
            const btn = document.getElementById('sorgula-btn');
            btn.className = 'btn-ai';
            btn.innerHTML = '<i class="fas fa-robot"></i> AI ile Konuş';
        }

        // Instagram arayüzü göster
        function showInstagramInterface(api) {
            updateDynamicFields(api);
            document.getElementById('main-form-container').style.display = 'block';
            document.getElementById('instagram-stats-section').style.display = 'block';
            
            // Butonu Instagram moduna çevir
            const btn = document.getElementById('sorgula-btn');
            btn.className = 'btn-instagram';
            btn.innerHTML = '<i class="fab fa-instagram"></i> İşlemi Başlat';
            
            // Rastgele istatistikler oluştur (demo)
            document.getElementById('followers-count').textContent = Math.floor(Math.random() * 10000) + 500;
            document.getElementById('likes-count').textContent = Math.floor(Math.random() * 5000) + 200;
            document.getElementById('comments-count').textContent = Math.floor(Math.random() * 1000) + 50;
            document.getElementById('engagement-rate').textContent = (Math.random() * 10 + 2).toFixed(1) + '%';
        }

        // Ödeme arayüzü göster
        function showPaymentInterface(api) {
            updateDynamicFields(api);
            document.getElementById('main-form-container').style.display = 'block';
            document.getElementById('payment-section').style.display = 'block';
            
            // Kart numarası formatlama
            document.getElementById('cc').addEventListener('input', function(e) {
                let value = e.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
                let formattedValue = value.match(/.{1,4}/g)?.join(' ');
                if (formattedValue) {
                    e.target.value = formattedValue;
                }
            });
        }

        // Parametresiz komut arayüzü göster
        function showNoCommandInterface(api) {
            document.getElementById('main-form-container').style.display = 'block';
            document.getElementById('dynamic-fields').innerHTML = `
                <div class="form-group" style="grid-column: 1 / -1;">
                    <div style="text-align: center; padding: 20px; background: rgba(255,77,255,0.1); border-radius: 8px;">
                        <i class="fas fa-bolt" style="font-size: 48px; color: #ff4dff; margin-bottom: 15px;"></i>
                        <h3 style="color: #ff4dff; margin-bottom: 10px;">${api.name}</h3>
                        <p style="color: #e6f9ff;">Bu işlem parametre gerektirmez. Sorgula butonuna tıklayarak işlemi başlatabilirsiniz.</p>
                    </div>
                </div>
            `;
            
            // Butonu özel renk yap
            const btn = document.getElementById('sorgula-btn');
            btn.className = 'btn-ai';
            btn.innerHTML = `<i class="fas fa-play"></i> ${api.name} Başlat`;
        }

        // Dinamik input alanlarını güncelle
        function updateDynamicFields(selectedApi) {
            const dynamicFields = document.getElementById('dynamic-fields');
            dynamicFields.innerHTML = '';

            if (!selectedApi) return;

            selectedApi.params.forEach(param => {
                const fieldGroup = document.createElement('div');
                fieldGroup.className = 'form-group';
                
                const label = document.createElement('label');
                label.textContent = getParamLabel(param);
                label.htmlFor = `param-${param}`;
                
                let input;
                if (param === 'message') {
                    input = document.createElement('textarea');
                    input.rows = 4;
                    input.placeholder = 'AI\'ya sormak istediğiniz soruyu yazın...';
                } else {
                    input = document.createElement('input');
                    input.type = 'text';
                    input.placeholder = getParamPlaceholder(param);
                }
                
                input.id = `param-${param}`;
                input.name = param;
                input.required = true;
                
                // Özel validasyonlar
                if (param === 'tc') {
                    input.pattern = '[0-9]{11}';
                    input.maxLength = 11;
                    input.minLength = 11;
                } else if (param === 'gsm') {
                    input.pattern = '[0-9]{10}';
                    input.maxLength = 10;
                    input.minLength = 10;
                } else if (param === 'miktar') {
                    input.type = 'number';
                    input.min = '1';
                    input.max = '10000';
                } else if (param === 'cc') {
                    input.maxLength = 19;
                } else if (param === 'cvv') {
                    input.maxLength = 3;
                    input.pattern = '[0-9]{3}';
                } else if (param === 'sayi') {
                    input.type = 'number';
                    input.min = '1';
                    input.max = '100';
                }

                fieldGroup.appendChild(label);
                fieldGroup.appendChild(input);
                dynamicFields.appendChild(fieldGroup);
            });
        }

        // AI mesaj gönder
        function sendAIMessage() {
            const input = document.getElementById('ai-chat-input');
            const message = input.value.trim();
            
            if (!message) return;

            // Kullanıcı mesajını ekle
            addChatMessage('user', message);
            input.value = '';

            // Loading göster
            document.getElementById('loading').style.display = 'block';

            // 10 saniye sonra düşünme animasyonunu göster
            thinkingTimeout = setTimeout(() => {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('ai-thinking').style.display = 'flex';
            }, 10000); // 10 saniye

            // 15 saniye sonra yazıyor animasyonunu göster
            typingTimeout = setTimeout(() => {
                document.getElementById('ai-thinking').style.display = 'none';
                document.getElementById('ai-typing').style.display = 'flex';
            }, 15000); // 15 saniye

            // Gerçek AI API'sine istek gönder
            fetch('/api/sorgu', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    api: currentApi,
                    message: message
                })
            })
            .then(response => response.json())
            .then(result => {
                // Animasyonları temizle
                clearTimeout(thinkingTimeout);
                clearTimeout(typingTimeout);
                document.getElementById('loading').style.display = 'none';
                document.getElementById('ai-thinking').style.display = 'none';
                document.getElementById('ai-typing').style.display = 'none';
                
                if (result.success) {
                    let aiResponse = '';
                    if (typeof result.data === 'string') {
                        aiResponse = result.data;
                    } else if (result.data && result.data.response) {
                        aiResponse = result.data.response;
                    } else {
                        aiResponse = JSON.stringify(result.data, null, 2);
                    }
                    addChatMessage('ai', aiResponse);
                } else {
                    addChatMessage('ai', 'Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.');
                }
            })
            .catch(error => {
                // Animasyonları temizle
                clearTimeout(thinkingTimeout);
                clearTimeout(typingTimeout);
                document.getElementById('loading').style.display = 'none';
                document.getElementById('ai-thinking').style.display = 'none';
                document.getElementById('ai-typing').style.display = 'none';
                
                addChatMessage('ai', 'Bağlantı hatası. Lütfen daha sonra tekrar deneyin.');
            });
        }

        // Ödeme işlemi
        function processPayment(e) {
            e.preventDefault();
            
            const cc = document.getElementById('cc').value.replace(/\s+/g, '');
            const ay = document.getElementById('ay').value;
            const yil = document.getElementById('yil').value;
            const cvv = document.getElementById('cvv').value;

            // Basit validasyon
            if (cc.length !== 16) {
                showError('Geçerli bir kart numarası girin (16 haneli)');
                return;
            }

            if (cvv.length !== 3) {
                showError('Geçerli bir CVV girin (3 haneli)');
                return;
            }

            document.getElementById('loading').style.display = 'block';

            // Ödeme API'sine istek gönder
            fetch('/api/sorgu', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    api: currentApi,
                    cc: cc,
                    ay: ay,
                    yil: yil,
                    cvv: cvv
                })
            })
            .then(response => response.json())
            .then(result => {
                document.getElementById('loading').style.display = 'none';
                
                if (result.success) {
                    showSuccess('Ödeme işlemi başarılı!');
                    // Sonuçları göster
                    document.getElementById('result-section').style.display = 'block';
                    document.getElementById('result-title').textContent = 'Ödeme Sonucu';
                    parseAndDisplayResults(result.data, currentApi);
                } else {
                    showError(result.error || 'Ödeme işlemi başarısız');
                }
            })
            .catch(error => {
                document.getElementById('loading').style.display = 'none';
                showError('Ödeme işlemi sırasında bir hata oluştu: ' + error.message);
            });
        }

        // Sohbet mesajı ekle
        function addChatMessage(sender, content) {
            const chatContainer = document.getElementById('ai-chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `chat-message ${sender}-message`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            chatContainer.appendChild(messageDiv);
            
            // Scroll en alta kaydır
            chatContainer.scrollTop = chatContainer.scrollHeight;
            
            // Geçmişe ekle
            aiChatHistory.push({ sender, content, timestamp: new Date() });
        }

        // Form gönderimi
        document.getElementById('sorgu-form').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            if (!currentApi) {
                showError('Sorgu türü bulunamadı!');
                return;
            }
            
            const selectedApi = APIS.find(api => api.value === currentApi);
            
            // Parametreleri topla
            const params = {};
            selectedApi.params.forEach(param => {
                const input = document.getElementById(`param-${param}`);
                if (input) {
                    let value = input.value.trim();
                    
                    // Özel formatlamalar
                    if (param === 'kullanici' && value && !value.startsWith('@')) {
                        value = value.replace('@', '');
                    }
                    
                    params[param] = value;
                }
            });
            
            // Zorunlu alan kontrolü (parametresiz komutlar hariç)
            if (selectedApi.type !== 'nocommand') {
                for (const param of selectedApi.params) {
                    if (!params[param]) {
                        showError(`Lütfen ${getParamLabel(param)} alanını doldurun!`);
                        return;
                    }
                }
            }
            
            // TC format kontrolü
            if (params.tc && !/^[0-9]{11}$/.test(params.tc)) {
                showError('Geçerli bir TC kimlik numarası girin! (11 haneli)');
                return;
            }
            
            // GSM format kontrolü
            if (params.gsm && !/^[0-9]{10}$/.test(params.gsm)) {
                showError('Geçerli bir GSM numarası girin! (10 haneli)');
                return;
            }
            
            // Loading göster
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result-section').style.display = 'none';
            document.getElementById('error-section').style.display = 'none';
            document.getElementById('info-grid').style.display = 'none';
            
            try {
                // API isteği
                const response = await fetch('/api/sorgu', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        api: currentApi,
                        ...params
                    })
                });

                const result = await response.json();

                console.log("API Response:", result);

                // Sonuçları göster
                document.getElementById('loading').style.display = 'none';
                
                if (result.success) {
                    showSuccess('Sorgulama başarılı!');
                    document.getElementById('result-section').style.display = 'block';
                    document.getElementById('result-title').textContent = `${currentApi} Sonuçları`;
                    
                    // Sonuçları işle ve göster
                    parseAndDisplayResults(result.data, currentApi);
                } else {
                    showError(result.error || 'Sorgulama sırasında bir hata oluştu');
                }
                
            } catch (error) {
                document.getElementById('loading').style.display = 'none';
                showError('Network hatası: ' + error.message);
            }
        });

        // Parametre etiketlerini belirle
        function getParamLabel(param) {
            const labels = {
                'ad': 'Ad',
                'soyad': 'Soyad',
                'tc': 'TC Kimlik No',
                'gsm': 'GSM Numarası',
                'kullanici': 'Kullanıcı Adı',
                'domain': 'IP/Domain',
                'url': 'URL',
                'sehir': 'Şehir',
                'method': 'Şifreleme Methodu',
                'password': 'Şifre',
                'il': 'İl',
                'ada': 'Ada',
                'parsel': 'Parsel',
                'vergi': 'Vergi No',
                'unvan': 'Firma Ünvanı',
                'site': 'Site URL',
                'okulno': 'Okul Numarası',
                'message': 'AI Sorusu',
                'username': 'Kullanıcı Adı',
                'miktar': 'Miktar',
                'cc': 'Kart Numarası',
                'ay': 'Son Kullanma Ayı',
                'yil': 'Son Kullanma Yılı',
                'cvv': 'CVV',
                'mail': 'E-posta Adresi',
                'sayi': 'Sonuç Sayısı'
            };
            return labels[param] || param;
        }

        // Parametre placeholder'larını belirle
        function getParamPlaceholder(param) {
            const placeholders = {
                'ad': 'Adınızı girin',
                'soyad': 'Soyadınızı girin',
                'tc': '11 haneli TC kimlik no',
                'gsm': '10 haneli GSM numarası',
                'kullanici': 'Kullanıcı adı (@ işareti olmadan)',
                'domain': 'IP adresi veya domain',
                'url': 'Web sitesi URL',
                'sehir': 'Şehir adı',
                'method': 'MD5, SHA1, SHA256 vb.',
                'password': 'Şifrenizi girin',
                'il': 'İl adı',
                'ada': 'Ada numarası',
                'parsel': 'Parsel numarası',
                'vergi': 'Vergi numarası',
                'unvan': 'Firma ünvanı',
                'site': 'Site adresi',
                'okulno': 'Okul numarası',
                'message': 'AI\'ya sormak istediğiniz soru...',
                'username': 'Instagram kullanıcı adı',
                'miktar': 'İstenilen miktar',
                'cc': '1234 5678 9012 3456',
                'ay': 'MM',
                'yil': 'YY',
                'cvv': '123',
                'mail': 'ornek@gmail.com',
                'sayi': '1-100 arası sayı'
            };
            return placeholders[param] || ` ${param} değerini girin`;
        }

        // Sonuçları işle ve göster
        function parseAndDisplayResults(data, apiName) {
            const tableBody = document.getElementById('table-body');
            const tableHead = document.getElementById('table-head');
            const infoGrid = document.getElementById('info-grid');
            
            tableBody.innerHTML = '';
            tableHead.innerHTML = '';
            infoGrid.innerHTML = '';
            
            let results = [];
            let isGridPreferred = false;
            
            console.log("parseAndDisplayResults data:", data);
            
            // API yanıtına göre veriyi işle
            if (data && typeof data === 'object') {
                if (data.data && Array.isArray(data.data)) {
                    results = data.data;
                } else if (data.response && data.response.data && Array.isArray(data.response.data)) {
                    results = data.response.data;
                } else if (data.data && typeof data.data === 'object') {
                    // Tekil obje için
                    results = [data.data];
                    isGridPreferred = true;
                } else if (Array.isArray(data)) {
                    results = data;
                } else {
                    results = [data];
                    isGridPreferred = true;
                }
            }
            
            console.log("Processed results:", results);
            
            if (results.length === 0) {
                showError('Sorgu sonucu bulunamadı');
                return;
            }
            
            // İlk item'dan sütunları belirle
            const firstItem = results[0];
            const columns = Object.keys(firstItem);
            
            // Grid için IP sorguları gibi belirli API'ler
            if (isGridPreferred || apiName.includes('IP') || apiName.includes('Whois') || apiName.includes('DNS')) {
                displayAsGrid(firstItem);
                document.getElementById('info-grid').style.display = 'grid';
            } else {
                // Tablo gösterimi
                displayAsTable(results, columns);
            }
        }

        // Grid olarak göster
        function displayAsGrid(data) {
            const infoGrid = document.getElementById('info-grid');
            
            Object.keys(data).forEach(key => {
                const value = data[key];
                if (value && value !== '-' && value !== null) {
                    const infoItem = document.createElement('div');
                    infoItem.className = 'info-item';
                    infoItem.innerHTML = `
                        <div class="info-label">${key}</div>
                        <div class="info-value">${String(value)}</div>
                    `;
                    infoGrid.appendChild(infoItem);
                }
            });
        }

        // Tablo olarak göster
        function displayAsTable(results, columns) {
            const tableBody = document.getElementById('table-body');
            const tableHead = document.getElementById('table-head');
            
            // Tablo başlıklarını oluştur
            const headerRow = document.createElement('tr');
            const copyHeader = document.createElement('th');
            copyHeader.textContent = 'Kopyala';
            headerRow.appendChild(copyHeader);
            
            columns.forEach(col => {
                const th = document.createElement('th');
                th.textContent = col;
                headerRow.appendChild(th);
            });
            tableHead.appendChild(headerRow);
            
            // Tablo verilerini oluştur
            results.forEach(item => {
                const row = document.createElement('tr');
                
                // Kopyala butonu
                const copyCell = document.createElement('td');
                const copyButton = document.createElement('button');
                copyButton.className = 'btn-copy';
                copyButton.innerHTML = '<i class="fas fa-copy"></i>';
                copyButton.title = 'Satırı Kopyala';
                copyButton.onclick = function() {
                    const rowText = columns.map(col => `${col}: ${item[col] || '-'}`).join(' | ');
                    navigator.clipboard.writeText(rowText).then(() => {
                        copyButton.innerHTML = '<i class="fas fa-check"></i>';
                        setTimeout(() => {
                            copyButton.innerHTML = '<i class="fas fa-copy"></i>';
                        }, 2000);
                    });
                };
                copyCell.appendChild(copyButton);
                row.appendChild(copyCell);
                
                // Veri hücreleri
                columns.forEach(col => {
                    const cell = document.createElement('td');
                    cell.textContent = item[col] || '-';
                    row.appendChild(cell);
                });
                
                tableBody.appendChild(row);
            });
        }

        function showError(message) {
            const errorSection = document.getElementById('error-section');
            errorSection.style.display = 'block';
            errorSection.className = 'error-message';
            errorSection.innerHTML = `<strong>Hata:</strong> ${message}`;
        }

        function showSuccess(message) {
            const errorSection = document.getElementById('error-section');
            errorSection.style.display = 'block';
            errorSection.className = 'success-message';
            errorSection.innerHTML = `<strong>Başarılı:</strong> ${message}`;
        }
    </script>
</body>
</html>
