#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ☁️  MNAENCA 2026 - PINK LUXURY EDITION  💗            ║
║     Ultimate Version - 10 Files                            ║
║                                                              ║
║  🔥  Firebase: bomk-9f6ec                                 ║
║  ☁️   Cloudinary: vt6hibdu / y66.ko                     ║
║  👑  Admin: jasim28v@gmail.com                           ║
║  🤖  Avatars: DiceBear Big Smile (Random)                 ║
║  💎  Design: Pink Glass Luxury                            ║
║                                                              ║
║  ✨  PREMIUM FEATURES:                                     ║
║     • 💬 TikTok-Style Comments with Replies              ║
║     • 📤 Professional Share System                       ║
║     • 👤 Enhanced Profile with Video Grid                ║
║     • 💰 Iraqi Dinar Earnings Wallet (Profile Only)      ║
║     • 💧 Watermark on Downloaded Videos                  ║
║     • 🔔 Notification System (Working 100%)              ║
║     • 🎬 Compact Video Grid with Views                   ║
║     • 🗑️  Delete Videos from Admin Panel                  ║
║     • 🖤 Parallax Cover                                   ║
║     • 💎 Glass Morphism Dark Layers                       ║
║     • 💗 Pink Story Rings                                ║
║     • ✨ Pink/Cyan Glow Effects                           ║
║     • 🌟 Smooth In-App Viewer (No Popups!)               ║
║     • 📱 Floating Bottom Nav with Search                 ║
║     • 🎥 Slide-Up Video Reveal Animation                 ║
║     • 🎤 Voice Messages in Chat                          ║
║     • توثيق + حظر + حذف فيديوهات + محفظة أرباح              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import shutil

# ═══════════════════════════════════════════════════════════
# ☁️ CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyAAiH5kBtNBfuRbXddoCuLet9IGMG2U7q0",
    "authDomain": "bomk-9f6ec.firebaseapp.com",
    "databaseURL": "https://bomk-9f6ec-default-rtdb.firebaseio.com",
    "projectId": "bomk-9f6ec",
    "storageBucket": "bomk-9f6ec.firebasestorage.app",
    "messagingSenderId": "743058000945",
    "appId": "1:743058000945:web:a862e1eecf7d3d98925910",
    "measurementId": "G-7F4W2H5Z3Y"
}

CLOUD_NAME = "vt6hibdu"
UPLOAD_PRESET = "y66.ko"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"
APP_NAME = "MNAENCA"
WATERMARK_TEXT = "☁️ MNAENCA"
WATERMARK_URL = "https://res.cloudinary.com/vt6hibdu/image/upload/v1/watermark_mnaenca"

# 💰 Iraqi Dinar Earnings Configuration (Profile Only)
VIEW_RATE_IQD = 100  # 100 دينار لكل مشاهدة
MIN_WITHDRAWAL_IQD = 10000  # الحد الأدنى للسحب 10,000 دينار
USD_TO_IQD = 1450  # سعر الصرف

# 💗 Pink Luxury Palette
PINK_COLORS_JS = """[
    "linear-gradient(135deg, #831843, #be185d, #ec4899)",
    "linear-gradient(135deg, #500724, #831843, #be185d)",
    "linear-gradient(135deg, #9d174d, #db2777, #f472b6)",
    "linear-gradient(135deg, #4a044e, #86198f, #d946ef)",
    "linear-gradient(135deg, #be185d, #f472b6, #fbcfe8)",
    "linear-gradient(135deg, #2d0a1e, #4a0d2e, #be185d)"
]"""

OUTPUT_DIR = "output"

# ═══════════════════════════════════════════════════════════
# 💙 UTILITY - دوال مساعدة
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    """حفظ ملف وحساب عدد الأسطر"""
    global TOTAL_LINES
    filepath = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else OUTPUT_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    """طباعة عنوان القسم"""
    print(f"\n{'='*60}")
    print(f"  ☁️  {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# ☁️ COMMON CSS - ستايل مشترك
# ═══════════════════════════════════════════════════════════

COMMON_CSS = """
    :root{
        --glass:rgba(236,72,153,0.03);
        --border:rgba(236,72,153,0.12);
        --accent:#ec4899;
        --accent2:#f472b6;
        --bg:#020617;
        --card:rgba(236,72,153,0.06);
        --danger:#ef4444;
        --success:#22c55e;
        --warning:#f59e0b;
        --gold:#fbbf24;
    }
    *{margin:0;padding:0;box-sizing:border-box}
    body{
        font-family:'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
        background:var(--bg);
        color:#fff;
        -webkit-tap-highlight-color:transparent;
        user-select:none;
        -webkit-user-select:none;
    }
    @keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
    @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
    @keyframes spin{to{transform:rotate(360deg)}}
    @keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}
    @keyframes slideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}
    @keyframes slideDown{from{transform:translateY(0)}to{transform:translateY(100%)}}
    @keyframes scaleIn{from{transform:scale(0.8);opacity:0}to{transform:scale(1);opacity:1}}
    @keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
    @keyframes pinkGlow{0%,100%{box-shadow:0 0 20px rgba(236,72,153,0.3)}50%{box-shadow:0 0 40px rgba(244,114,182,0.7)}}
    @keyframes goldGlow{0%,100%{box-shadow:0 0 20px rgba(251,191,36,0.3)}50%{box-shadow:0 0 40px rgba(251,191,36,0.7)}}
    .spinner{
        width:36px;height:36px;
        border:3px solid rgba(236,72,153,0.2);
        border-top-color:var(--accent);
        border-radius:50%;
        animation:spin 0.7s linear infinite;
        margin:30px auto;
    }
    .toast-msg{
        position:fixed;bottom:120px;left:50%;transform:translateX(-50%);
        background:rgba(2,6,23,0.95);padding:12px 24px;border-radius:30px;
        z-index:10000;border:1px solid rgba(236,72,153,0.3);font-size:13px;
        opacity:0;transition:opacity 0.3s;pointer-events:none;white-space:nowrap;
        box-shadow:0 8px 32px rgba(0,0,0,0.4);
    }
    .toast-msg.show{opacity:1}
    .overlay{
        position:fixed;inset:0;background:rgba(2,6,23,0.97);
        backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
        z-index:400;overflow-y:auto;
        animation:fadeIn 0.3s ease;
    }
    .overlay-header{
        display:flex;justify-content:space-between;align-items:center;
        padding:16px 20px;border-bottom:1px solid var(--border);
        position:sticky;top:0;background:rgba(2,6,23,0.9);
        backdrop-filter:blur(20px);z-index:5;
    }
    .overlay-header h3{font-weight:700;font-size:17px;display:flex;align-items:center;gap:8px}
    .btn-close-overlay{
        background:rgba(236,72,153,0.1);border:1px solid var(--border);
        color:#fff;width:36px;height:36px;border-radius:50%;
        display:flex;align-items:center;justify-content:center;
        cursor:pointer;font-size:16px;transition:all 0.3s;
    }
    .btn-close-overlay:hover{background:rgba(236,72,153,0.25);box-shadow:0 0 15px rgba(236,72,153,0.3)}
"""

# ═══════════════════════════════════════════════════════════
# ☁️ 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// ☁️ MNAENCA 2026 - Pink Luxury Configuration
// Firebase: bomk-9f6ec | Cloudinary: vt6hibdu
// ✨ PREMIUM: Comments + Share + Wallet (Profile) + Voice Chat

const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${{CLOUD_NAME}}/auto/upload`;
const CLOUDINARY_IMAGE_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${{CLOUD_NAME}}/image/upload`;
const CLOUDINARY_AUDIO_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${{CLOUD_NAME}}/video/upload`;

// ☁️ MNAENCA Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {PINK_COLORS_JS};

// 💰 Iraqi Dinar Earnings Settings (Profile Only)
const VIEW_RATE_IQD = {VIEW_RATE_IQD};
const MIN_WITHDRAWAL_IQD = {MIN_WITHDRAWAL_IQD};
const USD_TO_IQD = {USD_TO_IQD};

// ☁️ App Info
const APP_NAME = "{APP_NAME}";
const APP_VERSION = "2026.4";
const PRIMARY_COLOR = "#ec4899";
const SECONDARY_COLOR = "#f472b6";
const GOLD_COLOR = "#fbbf24";
const WATERMARK_TEXT = "{WATERMARK_TEXT}";
const WATERMARK_URL = "{WATERMARK_URL}";

console.log('💗 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #ec4899; font-size: 16px; font-weight: bold;');
console.log('💰 %cEarnings System Active - '+VIEW_RATE_IQD+' IQD/View (Profile Only)', 'color: #ec4899; font-size: 14px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# ═══════════════════════════════════════════════════════════
# ☁️ 2. auth.html - واجهة تسجيل دخول واشتراك فاخرة
# ═══════════════════════════════════════════════════════════

def build_auth():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        
        body {{
            min-height: 100vh;
            background: radial-gradient(ellipse at top, #1a0a14, #0d060c, #020617);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        
        /* الخلفية المتحركة */
        .bg-orb {{
            position: fixed;
            border-radius: 50%;
            filter: blur(130px);
            opacity: 0.25;
            animation: orbFloat 20s infinite alternate;
            pointer-events: none;
        }}
        .bg-orb:nth-child(1) {{ width: 400px; height: 400px; background: #ec4899; top: -100px; left: -100px; }}
        .bg-orb:nth-child(2) {{ width: 350px; height: 350px; background: #f472b6; bottom: -100px; right: -100px; animation-delay: 5s; }}
        .bg-orb:nth-child(3) {{ width: 300px; height: 300px; background: #db2777; top: 50%; left: 50%; animation-delay: 10s; }}
        
        @keyframes orbFloat {{
            0% {{ transform: translate(0, 0) scale(1); }}
            100% {{ transform: translate(50px, -50px) scale(1.3); }}
        }}
        
        /* الجسيمات العائمة */
        .particles {{
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }}
        .particle {{
            position: absolute;
            width: 4px;
            height: 4px;
            background: #f472b6;
            border-radius: 50%;
            animation: particleFloat 10s infinite linear;
            opacity: 0.3;
        }}
        @keyframes particleFloat {{
            0% {{ transform: translateY(100vh) rotate(0deg); opacity: 0; }}
            10% {{ opacity: 0.3; }}
            90% {{ opacity: 0.3; }}
            100% {{ transform: translateY(-100vh) rotate(720deg); opacity: 0; }}
        }}
        
        .card {{
            position: relative;
            z-index: 1;
            width: 90%;
            max-width: 440px;
            background: rgba(236, 72, 153, 0.03);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border-radius: 32px;
            padding: 40px 28px;
            border: 1px solid rgba(236, 72, 153, 0.2);
            box-shadow: 0 30px 70px rgba(236, 72, 153, 0.1), inset 0 0 30px rgba(236, 72, 153, 0.02);
            animation: fadeUp 0.8s ease;
            max-height: 90vh;
            overflow-y: auto;
        }}
        
        .card::-webkit-scrollbar {{
            width: 4px;
        }}
        .card::-webkit-scrollbar-thumb {{
            background: rgba(236, 72, 153, 0.3);
            border-radius: 10px;
        }}
        
        .logo-container {{
            text-align: center;
            margin-bottom: 24px;
        }}
        
        .logo {{
            width: 80px;
            height: 80px;
            margin: 0 auto 16px;
            background: linear-gradient(135deg, rgba(236, 72, 153, 0.3), rgba(244, 114, 182, 0.3));
            border-radius: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            border: 1px solid rgba(236, 72, 153, 0.2);
            animation: pinkGlow 3s ease-in-out infinite;
            position: relative;
        }}
        
        .logo::after {{
            content: '';
            position: absolute;
            inset: -3px;
            border-radius: 27px;
            background: linear-gradient(135deg, #ec4899, #f472b6, #ec4899);
            background-size: 200% 200%;
            animation: gradientShift 3s ease infinite;
            z-index: -1;
            opacity: 0.5;
        }}
        
        @keyframes gradientShift {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}
        
        h1 {{
            text-align: center;
            font-size: 38px;
            font-weight: 900;
            background: linear-gradient(to bottom, #fff, #fbcfe8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 4px;
            letter-spacing: 1px;
        }}
        
        .subtitle {{
            text-align: center;
            color: rgba(255, 255, 255, 0.4);
            font-size: 14px;
            margin-bottom: 20px;
            font-weight: 300;
        }}
        
        /* شريط الأرباح */
        .earn-banner {{
            text-align: center;
            margin-bottom: 24px;
            padding: 14px;
            background: linear-gradient(135deg, rgba(236, 72, 153, 0.1), rgba(244, 114, 182, 0.05));
            border: 1px solid rgba(236, 72, 153, 0.3);
            border-radius: 16px;
            font-size: 13px;
            color: #f472b6;
            animation: pinkGlow 2s ease-in-out infinite;
            font-weight: 500;
            position: relative;
            overflow: hidden;
        }}
        
        .earn-banner::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(244, 114, 182, 0.1), transparent);
            animation: shimmer 3s infinite;
        }}
        
        @keyframes shimmer {{
            0% {{ left: -100%; }}
            100% {{ left: 100%; }}
        }}
        
        /* أزرار التواصل الاجتماعي */
        .social-buttons {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 24px;
        }}
        
        .social-btn {{
            width: 100%;
            padding: 14px;
            border-radius: 50px;
            border: 1px solid var(--border);
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            position: relative;
            overflow: hidden;
        }}
        
        .social-btn.google {{
            background: rgba(255, 255, 255, 0.05);
            color: #fff;
            border-color: rgba(255, 255, 255, 0.2);
        }}
        
        .social-btn.google:hover {{
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }}
        
        .social-btn.facebook {{
            background: rgba(24, 119, 242, 0.15);
            color: #fff;
            border-color: rgba(24, 119, 242, 0.3);
        }}
        
        .social-btn.facebook:hover {{
            background: rgba(24, 119, 242, 0.25);
            border-color: rgba(24, 119, 242, 0.5);
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(24, 119, 242, 0.3);
        }}
        
        .social-btn i {{
            font-size: 20px;
        }}
        
        .social-btn.google i {{
            color: #EA4335;
        }}
        
        .social-btn.facebook i {{
            color: #1877F2;
        }}
        
        /* الفاصل */
        .divider {{
            display: flex;
            align-items: center;
            gap: 16px;
            margin: 24px 0;
            color: rgba(255, 255, 255, 0.3);
            font-size: 12px;
        }}
        
        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: rgba(236, 72, 153, 0.2);
        }}
        
        /* التبويبات */
        .tabs {{
            display: flex;
            gap: 4px;
            background: rgba(236, 72, 153, 0.06);
            border-radius: 40px;
            padding: 4px;
            margin-bottom: 24px;
            position: relative;
        }}
        
        .tab {{
            flex: 1;
            padding: 12px;
            background: none;
            border: none;
            color: rgba(255, 255, 255, 0.5);
            cursor: pointer;
            border-radius: 40px;
            font-size: 14px;
            transition: all 0.3s;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }}
        
        .tab.active {{
            background: linear-gradient(135deg, #ec4899, #f472b6);
            color: #fff;
            box-shadow: 0 8px 20px rgba(236, 72, 153, 0.4);
        }}
        
        /* النماذج */
        .form {{
            display: none;
            animation: fadeIn 0.4s ease;
        }}
        
        .form.active {{
            display: block;
        }}
        
        .input-group {{
            position: relative;
            margin-bottom: 16px;
        }}
        
        .input-group .input-icon {{
            position: absolute;
            right: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: rgba(255, 255, 255, 0.3);
            font-size: 16px;
            transition: color 0.3s;
        }}
        
        .input-group input {{
            width: 100%;
            padding: 15px 45px 15px 18px;
            border-radius: 50px;
            background: rgba(236, 72, 153, 0.04);
            border: 1px solid rgba(236, 72, 153, 0.15);
            color: #fff;
            font-size: 14px;
            outline: none;
            transition: all 0.4s;
            direction: rtl;
        }}
        
        .input-group input:focus {{
            border-color: rgba(236, 72, 153, 0.6);
            box-shadow: 0 0 20px rgba(236, 72, 153, 0.1);
            background: rgba(236, 72, 153, 0.08);
        }}
        
        .input-group input:focus + .input-icon,
        .input-group input:focus ~ .input-icon {{
            color: #ec4899;
        }}
        
        .input-group input::placeholder {{
            color: rgba(255, 255, 255, 0.3);
        }}
        
        .input-group input[type="email"],
        .input-group input[type="password"] {{
            direction: rtl;
            text-align: right;
        }}
        
        .btn-submit {{
            width: 100%;
            padding: 15px;
            margin-top: 8px;
            background: linear-gradient(135deg, #ec4899, #f472b6);
            border: none;
            border-radius: 50px;
            color: #fff;
            font-weight: bold;
            font-size: 15px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(236, 72, 153, 0.4);
            position: relative;
            overflow: hidden;
        }}
        
        .btn-submit::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }}
        
        .btn-submit:hover {{
            transform: translateY(-2px);
            box-shadow: 0 20px 40px rgba(236, 72, 153, 0.6);
        }}
        
        .btn-submit:hover::before {{
            left: 100%;
        }}
        
        .btn-submit:active {{
            transform: scale(0.97);
        }}
        
        .btn-submit:disabled {{
            opacity: 0.5;
            pointer-events: none;
        }}
        
        .msg {{
            text-align: center;
            color: #fca5a5;
            font-size: 13px;
            margin-top: 12px;
            min-height: 20px;
            transition: all 0.3s;
        }}
        
        .msg.success {{
            color: #4ade80;
        }}
        
        /* إظهار/إخفاء كلمة المرور */
        .toggle-password {{
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: rgba(255, 255, 255, 0.3);
            cursor: pointer;
            font-size: 16px;
            transition: color 0.3s;
            background: none;
            border: none;
        }}
        
        .toggle-password:hover {{
            color: #ec4899;
        }}
        
        /* التحميل */
        .loading-spinner {{
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin 0.7s linear infinite;
            margin-left: 8px;
        }}
    </style>
</head>
<body>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    
    <div class="particles" id="particles"></div>
    
    <div class="card">
        <div class="logo-container">
            <div class="logo">💗</div>
            <h1>MNAENCA</h1>
            <p class="subtitle">Pink Luxury 2026 ✨</p>
        </div>
        
        <div class="earn-banner">
            💰 اربح {VIEW_RATE_IQD} دينار عراقي لكل مشاهدة!
        </div>
        
        <!-- أزرار التواصل الاجتماعي -->
        <div class="social-buttons">
            <button class="social-btn google" onclick="signInWithGoogle()" id="btnGoogle">
                <i class="fab fa-google"></i>
                <span>المتابعة باستخدام Google</span>
            </button>
            <button class="social-btn facebook" onclick="signInWithFacebook()" id="btnFacebook">
                <i class="fab fa-facebook-f"></i>
                <span>المتابعة باستخدام Facebook</span>
            </button>
        </div>
        
        <div class="divider">
            <span>أو</span>
        </div>
        
        <!-- التبويبات -->
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')">
                <i class="fas fa-sign-in-alt"></i> دخول
            </button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')">
                <i class="fas fa-user-plus"></i> اشتراك
            </button>
        </div>
        
        <!-- نموذج تسجيل الدخول -->
        <div id="formLogin" class="form active">
            <div class="input-group">
                <input type="email" id="loginEmail" placeholder="البريد الإلكتروني" autocomplete="email">
                <i class="fas fa-envelope input-icon"></i>
            </div>
            
            <div class="input-group">
                <input type="password" id="loginPass" placeholder="كلمة المرور" autocomplete="current-password">
                <i class="fas fa-lock input-icon"></i>
                <button class="toggle-password" onclick="togglePasswordVisibility('loginPass', this)">
                    <i class="fas fa-eye"></i>
                </button>
            </div>
            
            <button id="btnLogin" onclick="doLogin()" class="btn-submit">
                <i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول
            </button>
            
            <div class="msg" id="loginMsg"></div>
            
            <div style="text-align: center; margin-top: 16px;">
                <a href="#" style="color: rgba(255,255,255,0.4); font-size: 12px; text-decoration: none;" onclick="event.preventDefault(); alert('سيتم إضافة هذه الميزة قريباً')">
                    نسيت كلمة المرور؟
                </a>
            </div>
        </div>
        
        <!-- نموذج الاشتراك -->
        <div id="formRegister" class="form">
            <div class="input-group">
                <input type="text" id="regName" placeholder="اسم المستخدم" autocomplete="username">
                <i class="fas fa-user input-icon"></i>
            </div>
            
            <div class="input-group">
                <input type="email" id="regEmail" placeholder="البريد الإلكتروني" autocomplete="email">
                <i class="fas fa-envelope input-icon"></i>
            </div>
            
            <div class="input-group">
                <input type="password" id="regPass" placeholder="كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
                <i class="fas fa-lock input-icon"></i>
                <button class="toggle-password" onclick="togglePasswordVisibility('regPass', this)">
                    <i class="fas fa-eye"></i>
                </button>
            </div>
            
            <button id="btnRegister" onclick="doRegister()" class="btn-submit">
                <i class="fas fa-heart"></i> إنشاء حساب
            </button>
            
            <div class="msg" id="regMsg"></div>
        </div>
    </div>
    
    <script src="firebase-config.js"></script>
    <script>
        // إنشاء الجسيمات العائمة
        function createParticles() {{
            const container = document.getElementById('particles');
            for(let i = 0; i < 20; i++) {{
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 10 + 's';
                particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
                particle.style.width = (Math.random() * 4 + 2) + 'px';
                particle.style.height = particle.style.width;
                container.appendChild(particle);
            }}
        }}
        createParticles();
        
        function switchTab(type) {{
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            
            if(type === 'login') {{
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            }} else {{
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }}
        }}
        
        function togglePasswordVisibility(inputId, btn) {{
            const input = document.getElementById(inputId);
            if(input.type === 'password') {{
                input.type = 'text';
                btn.innerHTML = '<i class="fas fa-eye-slash"></i>';
            }} else {{
                input.type = 'password';
                btn.innerHTML = '<i class="fas fa-eye"></i>';
            }}
        }}
        
        // تسجيل الدخول عبر Google
        async function signInWithGoogle() {{
            const btn = document.getElementById('btnGoogle');
            btn.disabled = true;
            btn.innerHTML = '<span class="loading-spinner"></span> جاري الاتصال...';
            
            try {{
                const provider = new firebase.auth.GoogleAuthProvider();
                provider.addScope('email');
                provider.addScope('profile');
                
                const result = await auth.signInWithPopup(provider);
                const user = result.user;
                
                // حفظ بيانات المستخدم إذا لم تكن موجودة
                const userSnap = await db.ref('users/' + user.uid).once('value');
                if(!userSnap.exists()) {{
                    await createUserProfile(user, {{
                        username: user.displayName || 'مستخدم',
                        email: user.email,
                        avatarUrl: user.photoURL || (DICEBEAR_URL + '?seed=' + user.uid),
                        hasCustomAvatar: !!user.photoURL
                    }});
                }}
                
                window.location.replace('index.html');
            }} catch(error) {{
                console.error('Google sign-in error:', error);
                btn.disabled = false;
                btn.innerHTML = '<i class="fab fa-google"></i> المتابعة باستخدام Google';
                
                if(error.code === 'auth/popup-closed-by-user') {{
                    showToast('❌ تم إغلاق نافذة تسجيل الدخول');
                }} else {{
                    showToast('❌ خطأ في تسجيل الدخول: ' + error.message);
                }}
            }}
        }}
        
        // تسجيل الدخول عبر Facebook
        async function signInWithFacebook() {{
            const btn = document.getElementById('btnFacebook');
            btn.disabled = true;
            btn.innerHTML = '<span class="loading-spinner"></span> جاري الاتصال...';
            
            try {{
                const provider = new firebase.auth.FacebookAuthProvider();
                provider.addScope('email');
                provider.addScope('public_profile');
                
                const result = await auth.signInWithPopup(provider);
                const user = result.user;
                
                // حفظ بيانات المستخدم إذا لم تكن موجودة
                const userSnap = await db.ref('users/' + user.uid).once('value');
                if(!userSnap.exists()) {{
                    await createUserProfile(user, {{
                        username: user.displayName || 'مستخدم',
                        email: user.email,
                        avatarUrl: user.photoURL || (DICEBEAR_URL + '?seed=' + user.uid),
                        hasCustomAvatar: !!user.photoURL
                    }});
                }}
                
                window.location.replace('index.html');
            }} catch(error) {{
                console.error('Facebook sign-in error:', error);
                btn.disabled = false;
                btn.innerHTML = '<i class="fab fa-facebook-f"></i> المتابعة باستخدام Facebook';
                
                if(error.code === 'auth/popup-closed-by-user') {{
                    showToast('❌ تم إغلاق نافذة تسجيل الدخول');
                }} else if(error.code === 'auth/account-exists-with-different-credential') {{
                    showToast('❌ يوجد حساب بنفس البريد الإلكتروني');
                }} else {{
                    showToast('❌ خطأ في تسجيل الدخول: ' + error.message);
                }}
            }}
        }}
        
        // إنشاء ملف تعريف للمستخدم
        async function createUserProfile(user, additionalData = {{}}) {{
            const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];
            const userData = {{
                username: additionalData.username || 'مستخدم',
                email: user.email || '',
                bio: '',
                website: '',
                location: '',
                contactEmail: user.email || '',
                avatarUrl: additionalData.avatarUrl || (DICEBEAR_URL + '?seed=' + user.uid),
                hasCustomAvatar: additionalData.hasCustomAvatar || false,
                coverImageUrl: '',
                hasCustomCover: false,
                coverColor: coverColor,
                followers: {{}},
                following: {{}},
                totalLikes: 0,
                isVerified: false,
                verifiedAt: null,
                verifiedBy: null,
                banned: false,
                createdAt: Date.now(),
                lastSeen: Date.now(),
                wallet: {{
                    balance: 5000,
                    totalEarned: 5000,
                    totalWithdrawn: 0,
                    pendingWithdrawal: 0,
                    totalViews: 0,
                    lastWithdrawal: null
                }}
            }};
            
            await db.ref('users/' + user.uid).set(userData);
        }}
        
        // تسجيل الدخول التقليدي
        async function doLogin() {{
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            
            if(!email || !password) {{
                msg.innerText = '❌ الرجاء ملء جميع الحقول';
                return;
            }}
            
            btn.disabled = true;
            btn.innerHTML = '<span class="loading-spinner"></span> جاري الدخول...';
            msg.innerText = '';
            msg.className = 'msg';
            
            try {{
                await auth.signInWithEmailAndPassword(email, password);
                window.location.replace('index.html');
            }} catch(error) {{
                btn.disabled = false;
                btn.innerHTML = '<i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول';
                
                switch(error.code) {{
                    case 'auth/user-not-found':
                        msg.innerText = '❌ لا يوجد حساب بهذا البريد';
                        break;
                    case 'auth/wrong-password':
                    case 'auth/invalid-credential':
                        msg.innerText = '❌ كلمة المرور غير صحيحة';
                        break;
                    case 'auth/invalid-email':
                        msg.innerText = '❌ بريد إلكتروني غير صالح';
                        break;
                    case 'auth/too-many-requests':
                        msg.innerText = '❌ محاولات كثيرة، حاول لاحقاً';
                        break;
                    default:
                        msg.innerText = '❌ خطأ: ' + error.message;
                }}
            }}
        }}
        
        // التسجيل التقليدي
        async function doRegister() {{
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            
            if(!username || !email || !password) {{
                msg.innerText = '❌ الرجاء ملء جميع الحقول';
                return;
            }}
            if(username.length < 3) {{
                msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل';
                return;
            }}
            if(password.length < 6) {{
                msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل';
                return;
            }}
            if(!email.includes('@') || !email.includes('.')) {{
                msg.innerText = '❌ بريد إلكتروني غير صالح';
                return;
            }}
            
            btn.disabled = true;
            btn.innerHTML = '<span class="loading-spinner"></span> جاري إنشاء الحساب...';
            msg.innerText = '';
            msg.className = 'msg';
            
            try {{
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const user = userCredential.user;
                
                await createUserProfile(user, {{
                    username: username,
                    email: email
                }});
                
                msg.innerText = '✅ تم إنشاء الحساب! +5000 دينار مكافأة ترحيبية 🎉';
                msg.className = 'msg success';
                
                setTimeout(() => {{
                    window.location.replace('index.html');
                }}, 1500);
                
            }} catch(error) {{
                btn.disabled = false;
                btn.innerHTML = '<i class="fas fa-heart"></i> إنشاء حساب';
                msg.className = 'msg';
                
                switch(error.code) {{
                    case 'auth/email-already-in-use':
                        msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل';
                        break;
                    case 'auth/weak-password':
                        msg.innerText = '❌ كلمة المرور ضعيفة جداً';
                        break;
                    case 'auth/invalid-email':
                        msg.innerText = '❌ بريد إلكتروني غير صالح';
                        break;
                    case 'auth/operation-not-allowed':
                        msg.innerText = '❌ التسجيل غير مفعل، راجع إعدادات Firebase';
                        break;
                    default:
                        msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
                }}
            }}
        }}
        
        // إدخال بالضغط على Enter
        document.querySelectorAll('input').forEach(input => {{
            input.addEventListener('keydown', function(e) {{
                if(e.key === 'Enter') {{
                    e.preventDefault();
                    if(document.getElementById('formLogin').classList.contains('active')) {{
                        doLogin();
                    }} else {{
                        doRegister();
                    }}
                }}
            }});
        }});
        
        // التحقق من حالة المستخدم
        auth.onAuthStateChanged(user => {{
            if(user) {{
                window.location.replace('index.html');
            }}
        }});
        
        function showToast(message) {{
            const toast = document.createElement('div');
            toast.className = 'toast-msg show';
            toast.innerText = message;
            document.body.appendChild(toast);
            
            setTimeout(() => {{
                toast.classList.remove('show');
                setTimeout(() => toast.remove(), 300);
            }}, 3000);
        }}
        
        console.log('💗 MNAENCA Auth Ready with Google & Facebook');
    </script>
</body>
</html>"""
# ═══════════════════════════════════════════════════════════
# ☁️ 3. index.html - الرئيسية مع بحث بدون محفظة
# ═══════════════════════════════════════════════════════════

def build_index():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💗 MNAENCA | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{height:100vh;overflow:hidden;}}
        
        #loaderScreen{{
            position:fixed;inset:0;z-index:9999;
            background:radial-gradient(ellipse at top, #1a0a14, #0d060c, #020617);
            display:flex;align-items:center;justify-content:center;
            flex-direction:column;gap:16px;
        }}
        .spinner-big{{
            width:50px;height:50px;
            border:4px solid rgba(236,72,153,0.2);
            border-top-color:var(--accent);
            border-radius:50%;
            animation:spin 0.8s linear infinite;
        }}

        #mainApp{{display:none;height:100vh;position:relative}}

        .topbar{{
            position:fixed;top:10px;left:10px;right:10px;z-index:100;
            display:flex;justify-content:space-between;align-items:center;
            padding:8px 16px;
            background:rgba(2,6,23,0.7);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            border:1px solid var(--border);
            border-radius:50px;
            box-shadow:0 8px 32px rgba(236,72,153,0.08);
        }}
        .logo-icon{{
            width:34px;height:34px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            font-weight:900;font-size:12px;
            animation:pinkGlow 2s ease-in-out infinite;
        }}
        .logo-text{{
            font-weight:800;font-size:17px;
            background:linear-gradient(to bottom,#fff,#fbcfe8);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            margin-left:8px;
        }}
        .tabs{{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}}
        .tab{{
            background:none;border:none;color:rgba(255,255,255,0.5);
            padding:7px 16px;cursor:pointer;border-radius:25px;
            font-size:13px;font-weight:500;transition:all 0.3s;
        }}
        .tab.active{{background:rgba(236,72,153,0.25);color:#fff}}
        .top-icons{{display:flex;gap:16px;align-items:center}}
        .top-icon{{
            background:none;border:none;color:rgba(255,255,255,0.7);
            font-size:18px;cursor:pointer;transition:all 0.3s;position:relative;
        }}
        .top-icon:hover{{color:var(--accent2)}}
        .notif-badge{{
            position:absolute;top:-6px;right:-6px;
            min-width:18px;height:18px;
            background:#ef4444;
            border-radius:10px;
            border:2px solid var(--bg);
            display:none;
            align-items:center;justify-content:center;
            font-size:9px;font-weight:bold;padding:0 5px;
        }}

        .videos-wrap{{
            height:100vh;overflow-y:scroll;
            scroll-snap-type:y mandatory;
            scrollbar-width:none;-ms-overflow-style:none;
        }}
        .videos-wrap::-webkit-scrollbar{{display:none}}
        .vid-card{{height:100vh;scroll-snap-align:start;position:relative;background:#000}}

        .vid-card video {{
            width:100%;height:100%;object-fit:cover;
            opacity:0;transform:translateY(60px);
            transition:opacity 0.6s ease,transform 0.6s cubic-bezier(0.16,1,0.3,1);
        }}
        .vid-card.active video {{opacity:1;transform:translateY(0)}}

        .vid-info{{
            position:absolute;bottom:90px;left:14px;right:80px;z-index:20;
            text-shadow:0 2px 10px rgba(0,0,0,0.8);
        }}
        .author-row{{display:flex;align-items:center;gap:10px;margin-bottom:6px}}
        .author-avatar{{
            width:50px;height:50px;border-radius:50%;overflow:hidden;
            cursor:pointer;position:relative;
            background:linear-gradient(135deg, #ec4899, #f472b6, #fbcfe8);
            padding:3px;
            animation:pinkStoryRing 3s ease-in-out infinite;
            flex-shrink:0;
        }}
        @keyframes pinkStoryRing{{0%,100%{{box-shadow:0 0 15px rgba(236,72,153,0.4)}}50%{{box-shadow:0 0 25px rgba(244,114,182,0.8)}}}}
        .author-avatar img{{width:100%;height:100%;object-fit:cover;border-radius:50%;border:2px solid var(--bg)}}
        .author-name{{
            font-weight:700;font-size:15px;cursor:pointer;
            display:flex;align-items:center;gap:6px;flex-wrap:wrap;
        }}
        .verified-badge-main{{
            background:linear-gradient(135deg, #ec4899, #f472b6);
            color:#fff;font-size:10px;padding:2px 5px;border-radius:50%;
            display:inline-flex;align-items:center;justify-content:center;
            width:18px;height:18px;font-weight:bold;
            box-shadow:0 0 12px rgba(244,114,182,0.6);
        }}
        .btn-follow{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            padding:5px 14px;border-radius:20px;font-size:11px;
            font-weight:700;border:none;color:#fff;cursor:pointer;
            box-shadow:0 4px 15px rgba(236,72,153,0.4);
            transition:all 0.3s;white-space:nowrap;
        }}
        .btn-follow:hover{{box-shadow:0 8px 25px rgba(236,72,153,0.7);transform:translateY(-1px)}}
        .caption{{font-size:14px;margin-bottom:5px;line-height:1.4}}
        .tag{{color:var(--accent2);cursor:pointer;font-weight:500}}
        .music{{font-size:12px;opacity:0.8;display:flex;align-items:center;gap:6px;cursor:pointer}}
        .music-wave{{display:flex;gap:2px;align-items:flex-end;height:16px}}
        .music-wave span{{width:2px;background:var(--accent2);border-radius:1px;animation:musicWave 1s ease-in-out infinite}}
        .music-wave span:nth-child(1){{height:8px;animation-delay:0s}}
        .music-wave span:nth-child(2){{height:14px;animation-delay:0.15s}}
        .music-wave span:nth-child(3){{height:6px;animation-delay:0.3s}}
        .music-wave span:nth-child(4){{height:12px;animation-delay:0.45s}}
        .music-wave span:nth-child(5){{height:4px;animation-delay:0.6s}}
        @keyframes musicWave{{0%,100%{{transform:scaleY(1)}}50%{{transform:scaleY(1.8)}}}}

        /* 💧 Watermark */
        .watermark-overlay{{
            position:absolute;top:20px;right:20px;
            z-index:15;pointer-events:none;
            display:flex;align-items:center;gap:6px;
            opacity:0.6;
        }}
        .watermark-overlay span{{
            font-weight:700;font-size:13px;
            text-shadow:0 2px 8px rgba(0,0,0,0.6);
            color:#fff;
        }}
        .watermark-overlay img{{width:24px;height:24px;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.5))}}

        .side-btns{{
            position:absolute;right:14px;bottom:130px;
            display:flex;flex-direction:column;gap:22px;z-index:20;
        }}
        .sbtn{{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:#fff;cursor:pointer;
            font-size:10px;transition:transform 0.15s;
        }}
        .sbtn:active{{transform:scale(0.85)}}
        .sbtn i{{font-size:28px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}}
        .sbtn.liked i{{color:var(--accent);animation:likePop 0.4s ease}}
        @keyframes likePop{{0%{{transform:scale(1)}}50%{{transform:scale(1.4)}}100%{{transform:scale(1)}}}}
        .sbtn .cnt{{font-weight:700;font-size:11px}}

        /* 👁️ Views Display */
        .views-display{{
            display:flex;align-items:center;gap:4px;
            font-size:11px;opacity:0.8;margin-top:2px;
        }}
        .views-display i{{color:var(--accent2)}}

        /* 📤 Share Panel */
        .share-panel{{
            position:fixed;bottom:0;left:0;right:0;
            background:rgba(2,6,23,0.98);
            backdrop-filter:blur(40px);
            border-top:2px solid var(--accent);
            border-radius:24px 24px 0 0;
            padding:24px 20px 40px;
            z-index:500;
            transform:translateY(100%);
            transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .share-panel.show{{transform:translateY(0)}}
        .share-panel h3{{font-size:17px;font-weight:700;margin-bottom:20px;text-align:center;color:var(--accent2)}}
        .share-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}}
        .share-item{{
            display:flex;flex-direction:column;align-items:center;gap:8px;
            cursor:pointer;transition:transform 0.2s;
        }}
        .share-item:hover{{transform:scale(1.1)}}
        .share-item .share-icon{{
            width:56px;height:56px;border-radius:16px;
            display:flex;align-items:center;justify-content:center;
            font-size:24px;transition:all 0.3s;
        }}
        .share-item span{{font-size:11px;opacity:0.7}}
        .share-copy-row{{
            display:flex;gap:8px;align-items:center;
            background:rgba(236,72,153,0.06);border-radius:16px;
            padding:8px;border:1px solid var(--border);
        }}
        .share-copy-row input{{
            flex:1;padding:12px;border-radius:12px;
            background:rgba(236,72,153,0.04);border:1px solid var(--border);
            color:#fff;font-size:13px;outline:none;direction:ltr;
        }}
        .share-copy-row button{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;color:#fff;padding:12px 20px;border-radius:12px;
            font-weight:700;cursor:pointer;white-space:nowrap;
        }}

        /* 💬 TikTok Style Comments */
        .comments-panel{{
            position:fixed;bottom:0;left:0;right:0;
            background:rgba(2,6,23,0.98);
            backdrop-filter:blur(40px);
            border-top:2px solid var(--accent);
            border-radius:24px 24px 0 0;
            padding:0;
            z-index:500;
            max-height:70vh;
            display:flex;flex-direction:column;
            transform:translateY(100%);
            transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .comments-panel.show{{transform:translateY(0)}}
        .comments-header{{
            display:flex;justify-content:space-between;align-items:center;
            padding:16px 20px;border-bottom:1px solid var(--border);
            flex-shrink:0;
        }}
        .comments-header h3{{font-size:16px;font-weight:700;display:flex;align-items:center;gap:8px}}
        .comments-list{{flex:1;overflow-y:auto;padding:12px 16px}}
        .comment-item{{
            display:flex;gap:10px;padding:12px 0;
            border-bottom:1px solid rgba(236,72,153,0.06);
            animation:fadeIn 0.3s ease;
        }}
        .comment-avatar{{
            width:36px;height:36px;border-radius:50%;
            overflow:hidden;flex-shrink:0;
            border:2px solid rgba(236,72,153,0.2);
        }}
        .comment-avatar img{{width:100%;height:100%;object-fit:cover}}
        .comment-body{{flex:1;min-width:0}}
        .comment-user{{font-weight:600;font-size:13px;margin-bottom:2px;display:flex;align-items:center;gap:5px}}
        .comment-text{{font-size:13px;line-height:1.4;word-break:break-word}}
        .comment-actions{{display:flex;gap:16px;margin-top:6px;font-size:11px}}
        .comment-actions span{{cursor:pointer;opacity:0.6;display:flex;align-items:center;gap:4px;transition:opacity 0.2s}}
        .comment-actions span:hover{{opacity:1}}
        .comment-time{{font-size:10px;opacity:0.4}}
        .reply-item{{
            margin-right:46px;padding:8px 0;
            border-bottom:1px solid rgba(236,72,153,0.04);
            display:flex;gap:8px;
        }}
        .reply-item .comment-avatar{{width:28px;height:28px}}
        .comment-input-row{{
            display:flex;gap:8px;padding:12px 16px;
            border-top:1px solid var(--border);
            background:rgba(2,6,23,0.95);
            flex-shrink:0;
        }}
        .comment-input-row input{{
            flex:1;padding:12px 16px;border-radius:30px;
            background:rgba(236,72,153,0.04);border:1px solid var(--border);
            color:#fff;font-size:13px;outline:none;
        }}
        .comment-input-row button{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;color:#fff;padding:10px 18px;border-radius:30px;
            font-weight:700;cursor:pointer;white-space:nowrap;font-size:13px;
        }}

        /* ☁️ Fullscreen Video Player */
        .fullscreen-player {{
            position:fixed;top:0;left:0;width:100vw;height:100vh;
            background:#000;z-index:9999;display:flex;align-items:center;
            justify-content:center;opacity:0;pointer-events:none;
            transition:opacity 0.3s ease;flex-direction:column;
        }}
        .fullscreen-player.active {{opacity:1;pointer-events:auto}}
        .fullscreen-player video {{max-width:100%;max-height:85vh;object-fit:contain;cursor:pointer}}
        .player-controls{{
            position:absolute;bottom:100px;left:20px;right:20px;
            display:flex;align-items:center;justify-content:space-between;
            background:rgba(0,0,0,0.6);backdrop-filter:blur(20px);
            border-radius:50px;padding:10px 20px;
            border:1px solid rgba(236,72,153,0.3);z-index:10000;color:#fff;gap:12px;flex-wrap:wrap;
        }}
        .player-controls button{{background:none;border:none;color:#fff;font-size:20px;cursor:pointer;transition:color 0.2s;padding:5px}}
        .player-controls button:hover{{color:#f472b6}}
        .progress-wrap{{flex:1;display:flex;align-items:center;gap:8px;min-width:100px}}
        .progress-bar{{flex:1;height:4px;background:rgba(255,255,255,0.2);border-radius:4px;cursor:pointer;position:relative}}
        .progress-fill{{height:100%;background:linear-gradient(90deg,#ec4899,#f472b6);border-radius:4px;width:0%}}
        .close-player{{
            position:absolute;top:20px;left:20px;
            background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);
            border:1px solid rgba(236,72,153,0.4);color:#fff;
            width:44px;height:44px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            cursor:pointer;font-size:20px;z-index:10001;transition:all 0.3s;
        }}
        .close-player:hover{{background:rgba(236,72,153,0.3);box-shadow:0 0 20px rgba(236,72,153,0.5)}}

        /* 📱 FLOATING BOTTOM NAV */
        .nav-bottom{{
            position:fixed;bottom:12px;left:12px;right:12px;
            display:flex;justify-content:space-around;align-items:center;
            padding:8px 0;
            background:rgba(2,6,23,0.8);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            z-index:100;
            border:1px solid var(--border);
            border-radius:40px;
            box-shadow:0 -8px 32px rgba(236,72,153,0.06);
        }}
        .nav-item{{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:rgba(255,255,255,0.5);
            font-size:10px;cursor:pointer;transition:all 0.3s;text-decoration:none;
        }}
        .nav-item i{{font-size:22px}}
        .nav-item.active{{color:var(--accent2)}}
        .btn-add{{
            width:48px;height:48px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            margin-top:-30px;cursor:pointer;
            box-shadow:0 10px 30px rgba(236,72,153,0.6),0 0 40px rgba(236,72,153,0.2);
            border:none;color:#fff;font-size:20px;
            z-index:101;transition:all 0.3s;text-decoration:none;
        }}
        .btn-add:hover{{transform:scale(1.1);box-shadow:0 15px 40px rgba(236,72,153,0.8)}}
    </style>
</head>
<body>

<div id="loaderScreen">
    <div class="spinner-big"></div>
    <p style="color:rgba(255,255,255,0.5);font-size:15px">💗 MNAENCA جاري التحميل...</p>
</div>

<div id="mainApp">
    <div class="topbar">
        <div style="display:flex;align-items:center">
            <div class="logo-icon">💗</div>
            <span class="logo-text">MNAENCA</span>
        </div>
        <div class="tabs">
            <button class="tab" onclick="switchFeed('following')">متابَعين</button>
            <button class="tab active" onclick="switchFeed('forYou')">لك</button>
        </div>
        <div class="top-icons">
            <i class="fas fa-bell top-icon" onclick="openNotifs()"><span class="notif-badge" id="notifBadge"></span></i>
        </div>
    </div>

    <div class="videos-wrap" id="videosWrap">
        <div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
            <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#ec4899"></i>
            <p>لا توجد فيديوهات بعد</p>
            <p style="font-size:12px;opacity:0.5">ارفع أول فيديو واربح! 💰</p>
        </div>
    </div>

    <!-- ☁️ Fullscreen Video Player -->
    <div class="fullscreen-player" id="fullscreenPlayer" onclick="if(event.target===this)closePlayer()">
        <button class="close-player" onclick="closePlayer()"><i class="fas fa-times"></i></button>
        <video id="fullscreenVideo" controls playsinline></video>
        <div class="player-controls">
            <button onclick="skipTime(-10)"><i class="fas fa-backward"></i></button>
            <button id="btnPlayPause" onclick="togglePlayPause()"><i class="fas fa-pause"></i></button>
            <button onclick="skipTime(10)"><i class="fas fa-forward"></i></button>
            <div class="progress-wrap">
                <span id="currentTime">0:00</span>
                <div class="progress-bar" id="progressBar" onclick="seekVideo(event)">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <span id="duration">0:00</span>
            </div>
            <button onclick="toggleMutePlayer()"><i class="fas fa-volume-up" id="muteIcon"></i></button>
            <a id="downloadLink" href="#" download style="color:#f472b6;text-decoration:none;margin-left:10px;"><i class="fas fa-download"></i></a>
        </div>
    </div>

    <!-- 📤 Share Panel -->
    <div class="share-panel" id="sharePanel">
        <h3><i class="fas fa-share-alt"></i> مشاركة</h3>
        <div class="share-grid">
            <div class="share-item" onclick="shareTo('whatsapp')">
                <div class="share-icon" style="background:rgba(37,211,102,0.15);color:#25D366"><i class="fab fa-whatsapp"></i></div>
                <span>WhatsApp</span>
            </div>
            <div class="share-item" onclick="shareTo('telegram')">
                <div class="share-icon" style="background:rgba(0,136,204,0.15);color:#0088cc"><i class="fab fa-telegram"></i></div>
                <span>Telegram</span>
            </div>
            <div class="share-item" onclick="shareTo('facebook')">
                <div class="share-icon" style="background:rgba(24,119,242,0.15);color:#1877F2"><i class="fab fa-facebook"></i></div>
                <span>Facebook</span>
            </div>
            <div class="share-item" onclick="shareTo('twitter')">
                <div class="share-icon" style="background:rgba(29,161,242,0.15);color:#1DA1F2"><i class="fab fa-twitter"></i></div>
                <span>X</span>
            </div>
            <div class="share-item" onclick="shareTo('messenger')">
                <div class="share-icon" style="background:rgba(0,178,255,0.15);color:#00B2FF"><i class="fab fa-facebook-messenger"></i></div>
                <span>Messenger</span>
            </div>
            <div class="share-item" onclick="shareTo('email')">
                <div class="share-icon" style="background:rgba(234,67,53,0.15);color:#EA4335"><i class="fas fa-envelope"></i></div>
                <span>بريد</span>
            </div>
            <div class="share-item" onclick="shareTo('copy')">
                <div class="share-icon" style="background:rgba(236,72,153,0.15);color:#ec4899"><i class="fas fa-link"></i></div>
                <span>نسخ الرابط</span>
            </div>
            <div class="share-item" onclick="shareTo('embed')">
                <div class="share-icon" style="background:rgba(168,85,247,0.15);color:#a855f7"><i class="fas fa-code"></i></div>
                <span>تضمين</span>
            </div>
        </div>
        <div class="share-copy-row">
            <input type="text" id="shareUrlInput" value="" readonly dir="ltr">
            <button onclick="shareTo('copy')"><i class="fas fa-copy"></i> نسخ</button>
        </div>
    </div>
    <div class="overlay" id="shareOverlay" style="display:none;z-index:499" onclick="closeSharePanel()"></div>

    <!-- 💬 Comments Panel -->
    <div class="comments-panel" id="commentsPanel">
        <div class="comments-header">
            <h3><i class="fas fa-comments" style="color:var(--accent)"></i> التعليقات <span id="commentsCount" style="font-size:13px;opacity:0.5"></span></h3>
            <button class="btn-close-overlay" onclick="closeCommentsPanel()"><i class="fas fa-times"></i></button>
        </div>
        <div class="comments-list" id="commentsList"></div>
        <div class="comment-input-row">
            <input type="text" id="commentInput" placeholder="أضف تعليقاً..." onkeydown="if(event.key==='Enter')addComment()">
            <button onclick="addComment()"><i class="fas fa-paper-plane"></i> نشر</button>
        </div>
    </div>
    <div class="overlay" id="commentsOverlay" style="display:none;z-index:499" onclick="closeCommentsPanel()"></div>

    <div class="nav-bottom">
        <button class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <a href="search.html" class="nav-item"><i class="fas fa-search"></i><span>بحث</span></a>
        <a href="upload.html" class="btn-add"><i class="fas fa-plus"></i></a>
        <a href="chat.html" class="nav-item"><i class="fas fa-envelope"></i><span>رسائل</span></a>
        <a href="profile.html" class="nav-item"><i class="fas fa-user"></i><span>ملفي</span></a>
    </div>

    <div class="toast-msg" id="toast">✅ تم النسخ</div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null;
    let currentUserData = null;
    let allUsers = {{}};
    let allVideos = [];
    let allSounds = {{}};
    let isMuted = true;
    let currentFeed = 'forYou';
    let currentShareUrl = null;
    let playerVideo = null;
    let currentCommentVideoId = null;
    let replyingTo = null;

    // ☁️ Player Functions
    function openPlayer(url, title) {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        player.classList.add('active');
        video.src = url;
        video.load();
        video.play();
        document.getElementById('downloadLink').href = url;
        document.getElementById('downloadLink').download = title || 'video.mp4';
        playerVideo = video;
        video.onloadedmetadata = () => {{
            document.getElementById('duration').innerText = formatTime(video.duration);
            document.getElementById('muteIcon').className = video.muted ? 'fas fa-volume-mute' : 'fas fa-volume-up';
        }};
        video.ontimeupdate = () => {{
            const pct = (video.currentTime / video.duration) * 100;
            document.getElementById('progressFill').style.width = pct + '%';
            document.getElementById('currentTime').innerText = formatTime(video.currentTime);
        }};
    }}
    window.openPlayer = openPlayer;

    function closePlayer() {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        video.pause();video.src='';player.classList.remove('active');
    }}
    function togglePlayPause() {{
        const video = document.getElementById('fullscreenVideo');
        if(video.paused){{video.play();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-pause"></i>';}}
        else{{video.pause();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-play"></i>';}}
    }}
    function skipTime(sec) {{if(playerVideo)playerVideo.currentTime+=sec;}}
    function seekVideo(e) {{
        if(!playerVideo)return;
        const bar=document.getElementById('progressBar');
        const rect=bar.getBoundingClientRect();
        const pct=(e.clientX-rect.left)/rect.width;
        playerVideo.currentTime=pct*playerVideo.duration;
    }}
    function toggleMutePlayer() {{
        if(playerVideo){{playerVideo.muted=!playerVideo.muted;document.getElementById('muteIcon').className=playerVideo.muted?'fas fa-volume-mute':'fas fa-volume-up';}}
    }}

    // 📤 Share Functions
    function openSharePanel(url) {{
        currentShareUrl = url;
        document.getElementById('shareUrlInput').value = url;
        document.getElementById('sharePanel').classList.add('show');
        document.getElementById('shareOverlay').style.display = 'block';
    }}
    function closeSharePanel() {{
        document.getElementById('sharePanel').classList.remove('show');
        document.getElementById('shareOverlay').style.display = 'none';
    }}
    function shareTo(platform) {{
        const url = encodeURIComponent(currentShareUrl);
        const text = encodeURIComponent('شاهد هذا الفيديو على MNAENCA 💗');
        let shareUrl = '';
        switch(platform) {{
            case 'whatsapp': shareUrl = 'https://wa.me/?text=' + text + '%20' + url; break;
            case 'telegram': shareUrl = 'https://t.me/share/url?url=' + url + '&text=' + text; break;
            case 'facebook': shareUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + url; break;
            case 'twitter': shareUrl = 'https://twitter.com/intent/tweet?url=' + url + '&text=' + text; break;
            case 'messenger': shareUrl = 'https://www.facebook.com/dialog/send?link=' + url + '&app_id=0'; break;
            case 'email': shareUrl = 'mailto:?subject=' + text + '&body=' + url; break;
            case 'copy':
                navigator.clipboard.writeText(currentShareUrl).then(() => {{
                    showToast('✅ تم نسخ الرابط');
                    closeSharePanel();
                }});
                return;
            case 'embed':
                const embedCode = '<iframe src="' + currentShareUrl + '" width="100%" height="600" frameborder="0"></iframe>';
                navigator.clipboard.writeText(embedCode).then(() => {{
                    showToast('✅ تم نسخ كود التضمين');
                    closeSharePanel();
                }});
                return;
        }}
        if(shareUrl) window.open(shareUrl, '_blank');
        closeSharePanel();
    }}

    // 💬 Comments Functions
    async function openCommentsPanel(videoId) {{
        currentCommentVideoId = videoId;
        replyingTo = null;
        document.getElementById('commentsPanel').classList.add('show');
        document.getElementById('commentsOverlay').style.display = 'block';
        document.getElementById('commentInput').placeholder = 'أضف تعليقاً...';
        await loadComments();
    }}
    function closeCommentsPanel() {{
        document.getElementById('commentsPanel').classList.remove('show');
        document.getElementById('commentsOverlay').style.display = 'none';
        currentCommentVideoId = null;
        replyingTo = null;
    }}
    async function loadComments() {{
        if(!currentCommentVideoId) return;
        const snap = await db.ref('videos/' + currentCommentVideoId + '/comments').get();
        const comments = snap.val() || {{}};
        const commentsArr = Object.entries(comments).map(([id, c]) => ({{id, ...c}}));
        commentsArr.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
        document.getElementById('commentsCount').innerText = '(' + commentsArr.length + ')';
        const list = document.getElementById('commentsList');
        if(!commentsArr.length) {{
            list.innerHTML = '<div style="text-align:center;opacity:0.5;padding:30px"><i class="fas fa-comment-slash" style="font-size:32px;color:var(--accent);margin-bottom:8px;display:block"></i>لا توجد تعليقات</div>';
            return;
        }}
        list.innerHTML = commentsArr.map(c => {{
            const user = allUsers[c.userId] || {{username: c.username || 'مستخدم'}};
            const avatar = user.avatarUrl || (DICEBEAR_URL + '?seed=' + c.userId);
            const replies = c.replies ? Object.entries(c.replies).map(([rid, r]) => ({{id: rid, ...r}})) : [];
            replies.sort((a, b) => (a.timestamp || 0) - (b.timestamp || 0));
            let repliesHTML = '';
            if(replies.length) {{
                repliesHTML = replies.map(r => {{
                    const rUser = allUsers[r.userId] || {{username: r.username || 'مستخدم'}};
                    const rAvatar = rUser.avatarUrl || (DICEBEAR_URL + '?seed=' + r.userId);
                    return `<div class="reply-item">
                        <div class="comment-avatar"><img src="${{rAvatar}}" alt=""></div>
                        <div style="flex:1;min-width:0">
                            <div class="comment-user" style="font-size:12px">@${{rUser.username}} <span class="comment-time">${{formatTimeAgo(r.timestamp)}}</span></div>
                            <div class="comment-text" style="font-size:12px">${{r.text}}</div>
                        </div>
                    </div>`;
                }}).join('');
            }}
            return `<div class="comment-item">
                <div class="comment-avatar"><img src="${{avatar}}" alt=""></div>
                <div class="comment-body">
                    <div class="comment-user">@${{user.username}} ${{user.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : ''}} <span class="comment-time">${{formatTimeAgo(c.timestamp)}}</span></div>
                    <div class="comment-text">${{c.text}}</div>
                    <div class="comment-actions">
                        <span onclick="replyToComment('${{c.id}}', '@${{user.username}}')"><i class="fas fa-reply"></i> رد</span>
                        <span>${{c.likes || 0}} <i class="fas fa-heart"></i></span>
                    </div>
                    ${{repliesHTML}}
                </div>
            </div>`;
        }}).join('');
    }}
    function replyToComment(commentId, username) {{
        replyingTo = commentId;
        const input = document.getElementById('commentInput');
        input.placeholder = 'رد على ' + username + '...';
        input.focus();
    }}
    async function addComment() {{
        const input = document.getElementById('commentInput');
        const text = input.value.trim();
        if(!text || !currentCommentVideoId || !currentUser) return;
        const commentData = {{
            userId: currentUser.uid,
            username: currentUserData?.username || 'مستخدم',
            text: text,
            timestamp: Date.now(),
            likes: 0
        }};
        if(replyingTo) {{
            await db.ref('videos/' + currentCommentVideoId + '/comments/' + replyingTo + '/replies').push(commentData);
            replyingTo = null;
            input.placeholder = 'أضف تعليقاً...';
        }} else {{
            await db.ref('videos/' + currentCommentVideoId + '/comments').push(commentData);
            const videoSnap = await db.ref('videos/' + currentCommentVideoId).get();
            const video = videoSnap.val();
            if(video && video.sender !== currentUser.uid) {{
                sendNotification(video.sender, currentUserData?.username, 'علق على فيديو الخاص بك 💬');
            }}
        }}
        input.value = '';
        await loadComments();
    }}
    window.addComment = addComment;
    window.replyToComment = replyToComment;

    auth.onAuthStateChanged(async (user) => {{
        if(!user) {{ window.location.replace('auth.html'); return; }}
        currentUser = user;
        try {{
            const snap = await db.ref('users/' + user.uid).get();
            if(snap.exists()) {{
                currentUserData = {{uid: user.uid, ...snap.val()}};
            }}
        }} catch(e) {{ console.error('Error loading user:', e); }}

        db.ref('users').on('value', s => {{ allUsers = s.val() || {{}}; }});
        db.ref('videos').on('value', s => {{
            const data = s.val();
            if(!data) {{ allVideos = []; allSounds = {{}}; }}
            else {{
                allVideos = []; allSounds = {{}};
                Object.entries(data).forEach(([key, value]) => {{
                    allVideos.push({{id: key, ...value}});
                    if(value.music) allSounds[value.music] = (allSounds[value.music] || 0) + 1;
                }});
                allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
            }}
            renderVideos();
        }});

        db.ref('notifications/' + user.uid).on('value', s => {{
            const ns = s.val() || {{}};
            const badge = document.getElementById('notifBadge');
            if(badge) {{
                const count = Object.keys(ns).length;
                badge.style.display = count > 0 ? 'flex' : 'none';
                if(count > 0) badge.innerText = count;
            }}
        }});

        db.ref('presence/' + user.uid).set(true);
        db.ref('presence/' + user.uid).onDisconnect().remove();
        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        setInterval(() => {{ db.ref('users/' + user.uid + '/lastSeen').set(Date.now()); }}, 60000);

        document.getElementById('loaderScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'block';
    }});

    async function sendNotification(toUserId, fromUsername, msg) {{
        if(!currentUser) return;
        await db.ref('notifications/' + toUserId).push({{
            from: fromUsername || currentUserData?.username || 'مستخدم',
            msg: msg,
            timestamp: Date.now(),
            read: false
        }});
    }}

    function renderVideos() {{
        const container = document.getElementById('videosWrap');
        if(!container) return;
        let filtered = currentFeed === 'forYou' ? allVideos : allVideos.filter(v => currentUserData?.following?.[v.sender]);
        if(!filtered.length) {{
            container.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#ec4899"></i><p>${{currentFeed === 'forYou' ? 'لا توجد فيديوهات بعد' : 'تابع مستخدمين لرؤية فيديوهاتهم'}}</p></div>`;
            return;
        }}
        container.innerHTML = '';
        filtered.forEach(video => {{
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const user = allUsers[video.sender] || {{username: video.senderName || 'مستخدم'}};
            const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const viewsCount = video.views || 0;
            const caption = (video.description || '').replace(/#(\\w+)/g, '<span class="tag">#$1</span>');
            const avatarUrl = user.avatarUrl || (DICEBEAR_URL + '?seed=' + video.sender);
            const verifiedBadgeHtml = user.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : '';
            const musicHtml = video.music ? `<div class="music-wave">${{[1,2,3,4,5].map(()=>'<span></span>').join('')}}</div> ${{video.music}}` : 'Original Sound';

            const div = document.createElement('div');
            div.className = 'vid-card';
            div.innerHTML = `
                <div class="watermark-overlay"><span>💗 MNAENCA</span></div>
                <video loop playsinline muted data-src="${{video.url}}" poster="${{video.thumbnail || ''}}"></video>
                <div class="vid-info">
                    <div class="author-row">
                        <div class="author-avatar" onclick="openUserProfile('${{video.sender}}')">
                            <img src="${{avatarUrl}}" alt="avatar">
                        </div>
                        <div class="author-name">
                            <span onclick="openUserProfile('${{video.sender}}')">@${{user.username}}</span>
                            ${{verifiedBadgeHtml}}
                            ${{currentUser?.uid !== video.sender ? `<button class="btn-follow" onclick="event.stopPropagation();toggleFollow('${{video.sender}}', this)">${{isFollowing ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}}</button>` : ''}}
                        </div>
                    </div>
                    <div class="caption">${{caption}}</div>
                    <div class="music">${{musicHtml}}</div>
                    <div class="views-display"><i class="fas fa-eye"></i> ${{formatNumber(viewsCount)}} مشاهدة</div>
                </div>
                <div class="side-btns">
                    <button class="sbtn" onclick="toggleMute()"><i class="fas ${{isMuted ? 'fa-volume-mute' : 'fa-volume-up'}}"></i></button>
                    <button class="sbtn like-btn ${{isLiked ? 'liked' : ''}}" onclick="toggleLike('${{video.id}}', this)"><i class="fas fa-heart"></i><span class="cnt">${{video.likes || 0}}</span></button>
                    <button class="sbtn" onclick="openCommentsPanel('${{video.id}}')"><i class="fas fa-comment"></i><span class="cnt">${{commentsCount}}</span></button>
                    <button class="sbtn" onclick="openPlayer('${{video.url}}', 'video.mp4')"><i class="fas fa-expand"></i></button>
                    <button class="sbtn" onclick="openSharePanel('${{video.url}}')"><i class="fas fa-share"></i></button>
                </div>`;
            const videoEl = div.querySelector('video');
            videoEl.addEventListener('dblclick', e => {{
                e.stopPropagation();
                const likeBtn = div.querySelector('.like-btn');
                if(likeBtn) toggleLike(video.id, likeBtn);
            }});
            container.appendChild(div);
        }});
        initVideoObserver();
    }}

    function openUserProfile(userId) {{
        if(userId === currentUser?.uid) window.location.href = 'profile.html';
        else window.location.href = 'profile.html?uid=' + userId;
    }}

    function initVideoObserver() {{
        const observer = new IntersectionObserver(entries => {{
            entries.forEach(entry => {{
                const video = entry.target.querySelector('video');
                if(entry.isIntersecting) {{
                    entry.target.classList.add('active');
                    if(!video.src) video.src = video.dataset.src;
                    video.muted = isMuted;
                    video.play().catch(() => {{}});
                }} else {{
                    entry.target.classList.remove('active');
                    video.pause();
                }}
            }});
        }}, {{threshold: 0.65}});
        document.querySelectorAll('.vid-card').forEach(seg => observer.observe(seg));
    }}

    function toggleMute() {{ isMuted = !isMuted; document.querySelectorAll('video').forEach(v => v.muted = isMuted); }}
    function switchFeed(feed) {{ currentFeed = feed; document.querySelectorAll('.tab').forEach(t => t.classList.remove('active')); event.target.classList.add('active'); renderVideos(); }}

    async function toggleLike(videoId, btn) {{
        if(!currentUser) return;
        const ref = db.ref('videos/' + videoId);
        const snap = await ref.get();
        const video = snap.val();
        if(!video) return;
        let likes = video.likes || 0;
        let likedBy = video.likedBy || {{}};
        if(likedBy[currentUser.uid]) {{ likes--; delete likedBy[currentUser.uid]; }}
        else {{
            likes++; likedBy[currentUser.uid] = true;
            if(video.sender && video.sender !== currentUser.uid) {{
                sendNotification(video.sender, currentUserData?.username, 'أعجب بفيديو الخاص بك ❤️');
            }}
        }}
        await ref.update({{likes, likedBy}});
        btn.classList.toggle('liked');
        const countSpan = btn.querySelector('.cnt');
        if(countSpan) countSpan.innerText = likes;
    }}

    async function toggleFollow(userId, btn) {{
        if(!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId);
        const targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if(snap.exists()) {{ await userRef.remove(); await targetRef.remove(); btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة'; }}
        else {{
            await userRef.set(true); await targetRef.set(true); btn.innerHTML = '<i class="fas fa-user-check"></i> متابع';
            sendNotification(userId, currentUserData?.username, 'بدأ بمتابعتك 👤');
        }}
    }}

    async function openNotifs() {{
        const snap = await db.ref('notifications/' + currentUser.uid).once('value');
        const ns = snap.val() || {{}};
        const items = Object.values(ns).reverse();
        let notifHTML = '';
        if(!items.length) {{
            notifHTML = '<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';
        }} else {{
            items.forEach(n => {{
                notifHTML += `<div style="display:flex;gap:12px;padding:14px;border-bottom:1px solid rgba(236,72,153,0.1);align-items:center;animation:fadeIn 0.3s ease">
                    <div style="width:40px;height:40px;border-radius:50%;background:rgba(236,72,153,0.15);display:flex;align-items:center;justify-content:center;font-size:18px;color:#ec4899"><i class="fas fa-bell"></i></div>
                    <div><div style="font-weight:600">${{n.from || 'مستخدم'}}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${{n.msg || ''}}</div><div style="font-size:10px;opacity:0.3;margin-top:4px">${{new Date(n.timestamp).toLocaleString('ar-SA')}}</div></div></div>`;
            }});
        }}
        await db.ref('notifications/' + currentUser.uid).remove();
        const badge = document.getElementById('notifBadge');
        if(badge) badge.style.display = 'none';
        showOverlay('🔔 الإشعارات', notifHTML);
    }}

    function showOverlay(title, content) {{
        const id = 'overlay_' + Date.now();
        const html = `<div id="${{id}}" class="overlay"><div class="overlay-header"><h3>${{title}}</h3><button class="btn-close-overlay" onclick="document.getElementById('${{id}}').remove()"><i class="fas fa-times"></i></button></div><div style="padding:16px">${{content}}</div></div>`;
        document.body.insertAdjacentHTML('beforeend', html);
    }}

    function showToast(msg) {{
        const toast = document.getElementById('toast');
        toast.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2500);
    }}

    function formatTime(seconds) {{
        if(isNaN(seconds)) return '0:00';
        const m = Math.floor(seconds / 60);
        const s = Math.floor(seconds % 60);
        return m + ':' + (s < 10 ? '0' : '') + s;
    }}

    function formatTimeAgo(ts) {{
        if(!ts) return '';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        if(mins < 1) return 'الآن';
        if(mins < 60) return 'منذ ' + mins + ' د';
        if(hours < 24) return 'منذ ' + hours + ' س';
        if(days < 7) return 'منذ ' + days + ' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }}

    function formatNumber(num) {{
        return (num || 0).toLocaleString('ar-IQ');
    }}

    // Make functions globally accessible
    window.closePlayer = closePlayer;
    window.togglePlayPause = togglePlayPause;
    window.skipTime = skipTime;
    window.seekVideo = seekVideo;
    window.toggleMutePlayer = toggleMutePlayer;
    window.openSharePanel = openSharePanel;
    window.closeSharePanel = closeSharePanel;
    window.shareTo = shareTo;
    window.openCommentsPanel = openCommentsPanel;
    window.closeCommentsPanel = closeCommentsPanel;
    window.openUserProfile = openUserProfile;
    window.toggleFollow = toggleFollow;
    window.toggleLike = toggleLike;
    window.formatTime = formatTime;

    console.log('💗 MNAENCA Index Ready ✨');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 4. wallet.html - محفظة الأرباح (وردي)
# ═══════════════════════════════════════════════════════════

def build_wallet():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💰 MNAENCA | محفظة الأرباح</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        
        .header{{
            display:flex;align-items:center;gap:12px;padding:16px;
            border-bottom:1px solid var(--border);
            position:sticky;top:0;z-index:10;
            background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);
        }}
        .btn-back{{
            background:rgba(236,72,153,0.1);border:1px solid var(--border);
            width:38px;height:38px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            color:#fff;cursor:pointer;font-size:16px;text-decoration:none;
        }}
        
        .container{{max-width:500px;margin:0 auto;padding:20px}}
        
        .balance-card{{
            background:linear-gradient(135deg, rgba(236,72,153,0.15), rgba(244,114,182,0.1));
            border:2px solid rgba(236,72,153,0.4);
            border-radius:24px;padding:30px 20px;text-align:center;
            margin-bottom:20px;position:relative;overflow:hidden;
            animation:pinkGlow 3s ease-in-out infinite;
        }}
        .balance-label{{font-size:14px;opacity:0.7;margin-bottom:8px}}
        .balance-amount{{
            font-size:48px;font-weight:900;
            background:linear-gradient(to bottom, #f472b6, #ec4899);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        }}
        .balance-currency{{font-size:16px;opacity:0.7;margin-top:4px}}
        .balance-usd{{font-size:13px;color:var(--success);margin-top:8px}}
        
        .stats-grid{{
            display:grid;grid-template-columns:repeat(4,1fr);
            gap:10px;margin-bottom:20px;
        }}
        .stat-card{{
            background:var(--card);border:1px solid var(--border);
            border-radius:16px;padding:16px 10px;text-align:center;
            backdrop-filter:blur(10px);
        }}
        .stat-icon{{font-size:24px;margin-bottom:8px}}
        .stat-value{{font-size:18px;font-weight:700;color:var(--accent2)}}
        .stat-label{{font-size:10px;opacity:0.6;margin-top:4px}}
        
        .withdraw-btn{{
            width:100%;padding:16px;
            background:linear-gradient(135deg, #ec4899, #db2777);
            border:none;border-radius:20px;color:#fff;
            font-weight:800;font-size:16px;cursor:pointer;
            margin-bottom:20px;box-shadow:0 10px 30px rgba(236,72,153,0.4);
            transition:all 0.3s;
        }}
        .withdraw-btn:hover{{
            transform:translateY(-2px);
            box-shadow:0 15px 40px rgba(236,72,153,0.6);
        }}
        .withdraw-btn:disabled{{opacity:0.5;cursor:not-allowed}}
        
        .withdraw-form{{
            display:none;background:rgba(2,6,23,0.95);
            border:1px solid var(--border);border-radius:20px;
            padding:20px;margin-bottom:20px;
            animation:fadeIn 0.3s ease;
        }}
        .withdraw-form.show{{display:block}}
        .withdraw-form h3{{color:var(--accent2);margin-bottom:16px;text-align:center}}
        
        .form-group{{margin-bottom:14px}}
        .form-group label{{display:block;font-size:12px;opacity:0.7;margin-bottom:6px}}
        .form-group input,.form-group select{{
            width:100%;padding:12px 16px;border-radius:14px;
            background:rgba(236,72,153,0.04);border:1px solid var(--border);
            color:#fff;font-size:14px;outline:none;
        }}
        .form-group select option{{background:#0a1628;color:#fff}}
        
        .btn-submit-withdraw{{
            width:100%;padding:14px;
            background:linear-gradient(135deg, #ec4899, #db2777);
            border:none;border-radius:14px;color:#fff;
            font-weight:700;cursor:pointer;
        }}
        
        .transactions{{
            background:var(--card);border:1px solid var(--border);
            border-radius:20px;padding:16px;margin-bottom:80px;
        }}
        .transactions h3{{margin-bottom:12px;font-size:16px;display:flex;align-items:center;gap:8px}}
        
        .transaction-item{{
            display:flex;justify-content:space-between;align-items:center;
            padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.05);
        }}
        .transaction-item:last-child{{border-bottom:none}}
        
        .transaction-info{{display:flex;align-items:center;gap:10px}}
        .transaction-icon{{
            width:36px;height:36px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;font-size:16px;
        }}
        .transaction-icon.earning{{background:rgba(34,197,94,0.1);color:var(--success)}}
        .transaction-icon.withdrawal{{background:rgba(239,68,68,0.1);color:var(--danger)}}
        .transaction-icon.bonus{{background:rgba(236,72,153,0.1);color:var(--accent2)}}
        
        .transaction-amount{{font-weight:700}}
        .transaction-amount.positive{{color:var(--success)}}
        .transaction-amount.negative{{color:var(--danger)}}
        
        .toast-msg{{
            position:fixed;bottom:30px;left:50%;transform:translateX(-50%);
            background:rgba(2,6,23,0.95);padding:12px 24px;border-radius:30px;
            z-index:1000;border:1px solid rgba(236,72,153,0.3);
            font-size:13px;opacity:0;transition:opacity 0.3s;
            pointer-events:none;white-space:nowrap;
        }}
        .toast-msg.show{{opacity:1}}
    </style>
</head>
<body>

<div class="header">
    <a href="profile.html" class="btn-back"><i class="fas fa-arrow-right"></i></a>
    <h2><i class="fas fa-wallet" style="color:#ec4899"></i> محفظة الأرباح</h2>
</div>

<div class="container" id="walletContent" style="display:none">
    <div class="balance-card">
        <div class="balance-label">💰 الرصيد المتاح</div>
        <div class="balance-amount" id="balanceAmount">0</div>
        <div class="balance-currency">دينار عراقي</div>
        <div class="balance-usd" id="balanceUSD">≈ $0.00 USD</div>
    </div>
    
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-icon">👁️</div>
            <div class="stat-value" id="totalViews">0</div>
            <div class="stat-label">مشاهدة</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">💵</div>
            <div class="stat-value" id="totalEarned">0</div>
            <div class="stat-label">إجمالي الأرباح</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🏦</div>
            <div class="stat-value" id="totalWithdrawn">0</div>
            <div class="stat-label">تم سحبه</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">⏳</div>
            <div class="stat-value" id="pendingBalance">0</div>
            <div class="stat-label">قيد الانتظار</div>
        </div>
    </div>
    
    <button class="withdraw-btn" id="withdrawBtn" onclick="toggleWithdrawForm()">
        <i class="fas fa-money-bill-wave"></i> سحب الأرباح
    </button>
    
    <div class="withdraw-form" id="withdrawForm">
        <h3>💳 طلب سحب</h3>
        <div class="form-group">
            <label>المبلغ (دينار عراقي) - الحد الأدنى {MIN_WITHDRAWAL_IQD:,} د.ع</label>
            <input type="number" id="withdrawAmount" placeholder="أدخل المبلغ" min="{MIN_WITHDRAWAL_IQD}">
        </div>
        <div class="form-group">
            <label>طريقة الدفع</label>
            <select id="paymentMethod">
                <option value="zain_cash">📱 زين كاش</option>
                <option value="asia_hawala">🏦 آسيا حوالة</option>
                <option value="qi_card">💳 بطاقة كي كارد</option>
                <option value="bank_transfer">🏛️ تحويل مصرفي</option>
                <option value="western_union">🌍 ويسترن يونيون</option>
            </select>
        </div>
        <div class="form-group">
            <label>تفاصيل الحساب</label>
            <input type="text" id="accountDetails" placeholder="رقم الحساب / الهاتف">
        </div>
        <button class="btn-submit-withdraw" onclick="submitWithdrawal()">
            <i class="fas fa-check-circle"></i> تقديم الطلب
        </button>
    </div>
    
    <div class="transactions">
        <h3><i class="fas fa-history" style="color:#ec4899"></i> سجل المعاملات</h3>
        <div id="transactionsList"></div>
    </div>
</div>

<div id="loadingSpinner" style="display:flex;align-items:center;justify-content:center;min-height:80vh">
    <div class="spinner"></div>
</div>

<div class="toast-msg" id="toastMsg">✅ تم</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null;
    let walletData = null;
    
    auth.onAuthStateChanged(async (user) => {{
        if(!user) {{ window.location.href = 'auth.html'; return; }}
        currentUser = user;
        await loadWallet();
    }});
    
    async function loadWallet() {{
        try {{
            const userSnap = await db.ref('users/' + currentUser.uid).once('value');
            const userData = userSnap.val() || {{}};
            walletData = userData.wallet || {{}};
            
            const balance = walletData.balance || 0;
            const totalEarned = walletData.totalEarned || 0;
            const totalWithdrawn = walletData.totalWithdrawn || 0;
            const pendingBalance = walletData.pendingWithdrawal || 0;
            const totalViews = walletData.totalViews || 0;
            
            document.getElementById('balanceAmount').innerText = formatNumber(balance);
            document.getElementById('balanceUSD').innerText = 
                `≈ ${{(balance / USD_TO_IQD).toFixed(2)}} USD`;
            document.getElementById('totalViews').innerText = formatNumber(totalViews);
            document.getElementById('totalEarned').innerText = formatNumber(totalEarned);
            document.getElementById('totalWithdrawn').innerText = formatNumber(totalWithdrawn);
            document.getElementById('pendingBalance').innerText = formatNumber(pendingBalance);
            
            if(balance < MIN_WITHDRAWAL_IQD) {{
                document.getElementById('withdrawBtn').disabled = true;
                document.getElementById('withdrawBtn').innerHTML = 
                    `<i class="fas fa-lock"></i> الحد الأدنى للسحب ${{formatNumber(MIN_WITHDRAWAL_IQD)}} د.ع`;
            }}
            
            await loadTransactions();
            
            document.getElementById('loadingSpinner').style.display = 'none';
            document.getElementById('walletContent').style.display = 'block';
        }} catch(error) {{
            console.error('Error loading wallet:', error);
            document.getElementById('loadingSpinner').style.display = 'none';
            document.getElementById('walletContent').style.display = 'block';
        }}
    }}
    
    async function loadTransactions() {{
        const transactionsSnap = await db.ref('transactions/' + currentUser.uid).once('value');
        const transactions = transactionsSnap.val() || {{}};
        const transactionsList = document.getElementById('transactionsList');
        
        const items = Object.entries(transactions)
            .sort(([, a], [, b]) => (b.timestamp || 0) - (a.timestamp || 0))
            .slice(0, 20);
        
        if(!items.length) {{
            transactionsList.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا توجد معاملات بعد</div>';
            return;
        }}
        
        transactionsList.innerHTML = items.map(([id, t]) => {{
            const isEarning = t.type === 'earning' || t.type === 'bonus';
            const icon = t.type === 'withdrawal' ? 'fa-arrow-up' : 'fa-arrow-down';
            const iconClass = t.type === 'withdrawal' ? 'withdrawal' : (t.type === 'bonus' ? 'bonus' : 'earning');
            const amountClass = isEarning ? 'positive' : 'negative';
            const amountPrefix = isEarning ? '+' : '-';
            
            return `
                <div class="transaction-item">
                    <div class="transaction-info">
                        <div class="transaction-icon ${{iconClass}}">
                            <i class="fas ${{icon}}"></i>
                        </div>
                        <div>
                            <div style="font-size:13px">${{t.description || t.type}}</div>
                            <div style="font-size:10px;opacity:0.5;margin-top:2px">${{new Date(t.timestamp).toLocaleString('ar-IQ')}}</div>
                        </div>
                    </div>
                    <div class="transaction-amount ${{amountClass}}">
                        ${{amountPrefix}}${{formatNumber(t.amount)}} د.ع
                    </div>
                </div>
            `;
        }}).join('');
    }}
    
    function toggleWithdrawForm() {{
        const form = document.getElementById('withdrawForm');
        form.classList.toggle('show');
    }}
    
    async function submitWithdrawal() {{
        const amount = parseInt(document.getElementById('withdrawAmount').value);
        const paymentMethod = document.getElementById('paymentMethod').value;
        const accountDetails = document.getElementById('accountDetails').value.trim();
        
        if(!amount || amount < MIN_WITHDRAWAL_IQD) {{
            showToast(`❌ الحد الأدنى للسحب ${{formatNumber(MIN_WITHDRAWAL_IQD)}} دينار`);
            return;
        }}
        
        if(!accountDetails) {{
            showToast('❌ الرجاء إدخال تفاصيل الحساب');
            return;
        }}
        
        if(amount > (walletData.balance || 0)) {{
            showToast('❌ الرصيد غير كافي');
            return;
        }}
        
        try {{
            const withdrawalData = {{
                userId: currentUser.uid,
                amount: amount,
                paymentMethod: paymentMethod,
                accountDetails: accountDetails,
                status: 'pending',
                timestamp: Date.now()
            }};
            
            await db.ref('withdrawals/' + currentUser.uid).push(withdrawalData);
            
            const newBalance = (walletData.balance || 0) - amount;
            await db.ref('users/' + currentUser.uid + '/wallet').update({{
                balance: newBalance,
                pendingWithdrawal: (walletData.pendingWithdrawal || 0) + amount,
                totalWithdrawn: (walletData.totalWithdrawn || 0) + amount,
                lastWithdrawal: Date.now()
            }});
            
            await db.ref('transactions/' + currentUser.uid).push({{
                type: 'withdrawal',
                amount: amount,
                description: 'طلب سحب - ' + paymentMethod,
                status: 'pending',
                timestamp: Date.now()
            }});
            
            showToast('✅ تم تقديم طلب السحب بنجاح');
            document.getElementById('withdrawAmount').value = '';
            document.getElementById('accountDetails').value = '';
            toggleWithdrawForm();
            await loadWallet();
        }} catch(error) {{
            showToast('❌ حدث خطأ في معالجة الطلب');
        }}
    }}
    
    function showToast(msg) {{
        const toast = document.getElementById('toastMsg');
        toast.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
    }}
    
    function formatNumber(num) {{
        return (num || 0).toLocaleString('ar-IQ');
    }}
    
    console.log('💰 MNAENCA Wallet Ready (Pink)');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 5. profile.html - ملف شخصي محترف مطور (وردي مع محفظة + فيديوهات داخلية + مشاهدات ولايكات)
# ═══════════════════════════════════════════════════════════════════════════════════

def build_profile():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | ملف شخصي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto;overflow-x:hidden;}}
        .cover-section{{position:relative;width:100%;height:280px;overflow:hidden;cursor:pointer}}
        .cover-img{{width:100%;height:130%;object-fit:cover;transition:transform 0.1s linear;transform:translateY(0)}}
        .cover-gradient{{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 30%,rgba(2,6,23,0.4) 60%,rgba(2,6,23,0.95) 100%);pointer-events:none;z-index:1}}
        .cover-glow{{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(236,72,153,0.15) 0%,transparent 70%);pointer-events:none;z-index:2}}
        .cover-edit-btn{{position:absolute;top:12px;left:12px;background:rgba(0,0,0,0.5);backdrop-filter:blur(15px);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:5;border:1px solid rgba(236,72,153,0.3);color:#fff;font-size:14px;transition:all 0.3s;box-shadow:0 4px 15px rgba(0,0,0,0.3)}}
        .cover-edit-btn:hover{{background:rgba(236,72,153,0.4);box-shadow:0 0 20px rgba(236,72,153,0.5)}}
        .btn-back{{position:fixed;top:20px;right:20px;background:rgba(0,0,0,0.5);backdrop-filter:blur(15px);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid var(--border);color:#fff;font-size:16px;transition:all 0.3s}}
        .btn-back:hover{{background:rgba(236,72,153,0.3);box-shadow:0 0 20px rgba(236,72,153,0.4)}}
        .avatar-wrap{{position:relative;z-index:2;margin-top:-60px;display:flex;justify-content:center}}
        .avatar-lg{{width:120px;height:120px;border-radius:50%;overflow:hidden;cursor:pointer;background:linear-gradient(135deg,#ec4899,#f472b6,#fbcfe8);padding:3px;box-shadow:0 0 30px rgba(236,72,153,0.4),0 0 60px rgba(236,72,153,0.1);animation:avatarPinkGlow 3s ease-in-out infinite}}
        @keyframes avatarPinkGlow{{0%,100%{{box-shadow:0 0 30px rgba(236,72,153,0.4),0 0 60px rgba(236,72,153,0.1)}}50%{{box-shadow:0 0 40px rgba(244,114,182,0.7),0 0 80px rgba(236,72,153,0.3)}}}}
        .avatar-lg img{{width:100%;height:100%;object-fit:cover;border-radius:50%;border:3px solid var(--bg)}}
        .avatar-edit-btn{{position:absolute;bottom:5px;right:5px;width:30px;height:30px;background:var(--accent);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;border:2px solid var(--bg);color:#fff;font-size:12px;box-shadow:0 0 15px rgba(236,72,153,0.5)}}
        .online-dot{{position:absolute;top:10px;right:10px;width:18px;height:18px;background:#22c55e;border-radius:50%;border:3px solid var(--bg);z-index:3;box-shadow:0 0 10px rgba(34,197,94,0.6)}}
        .profile-info{{padding:20px 20px 10px;text-align:center}}
        .username{{font-size:22px;font-weight:800;margin-bottom:4px;display:flex;align-items:center;justify-content:center;gap:8px}}
        .bio-text{{font-size:13px;opacity:0.7;margin-bottom:8px;max-width:320px;margin-left:auto;margin-right:auto;line-height:1.5}}
        .contact-info{{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:8px;font-size:12px}}
        .contact-info a{{color:var(--accent2);text-decoration:none;display:flex;align-items:center;gap:5px;background:var(--card);padding:6px 14px;border-radius:20px;border:1px solid var(--border);transition:all 0.3s}}
        .contact-info a:hover{{background:rgba(236,72,153,0.15);box-shadow:0 0 15px rgba(236,72,153,0.2)}}
        .last-seen{{font-size:11px;opacity:0.5;display:flex;align-items:center;justify-content:center;gap:5px;margin-top:6px}}
        .wallet-mini{{
            display:flex;align-items:center;justify-content:center;gap:8px;
            margin:10px 20px;padding:14px;
            background:linear-gradient(135deg,rgba(236,72,153,0.15),rgba(244,114,182,0.08));
            border:1px solid rgba(236,72,153,0.4);
            border-radius:16px;cursor:pointer;font-size:14px;font-weight:700;color:var(--accent2);
            animation:pinkGlow 2s ease-in-out infinite;
            transition:all 0.3s;position:relative;overflow:hidden;
        }}
        .wallet-mini::before{{
            content:'';position:absolute;inset:0;
            background:linear-gradient(90deg,transparent,rgba(236,72,153,0.2),transparent);
            animation:shimmer 3s infinite;
        }}
        @keyframes shimmer{{0%{{transform:translateX(-100%)}}100%{{transform:translateX(100%)}}}}
        .wallet-mini:hover{{background:rgba(236,72,153,0.25);transform:translateY(-2px)}}
        .stats-row{{display:flex;justify-content:center;gap:30px;margin:15px 20px;padding:18px;background:rgba(236,72,153,0.04);backdrop-filter:blur(20px);border-radius:20px;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.2)}}
        .stat-item{{text-align:center;cursor:pointer;transition:transform 0.2s}}
        .stat-item:hover{{transform:scale(1.1)}}
        .stat-val{{font-size:22px;font-weight:800;color:var(--accent2)}}
        .stat-lbl{{font-size:10px;opacity:0.6;margin-top:2px}}
        .action-btns{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0 20px 20px}}
        .btn{{background:rgba(236,72,153,0.06);border:1px solid var(--border);padding:10px 20px;border-radius:25px;color:#fff;cursor:pointer;font-size:13px;transition:all 0.3s;display:flex;align-items:center;gap:6px;backdrop-filter:blur(10px);text-decoration:none}}
        .btn:hover{{background:rgba(236,72,153,0.15);border-color:var(--accent);box-shadow:0 0 20px rgba(236,72,153,0.2)}}
        .btn-primary{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;font-weight:700;color:#fff;box-shadow:0 8px 25px rgba(236,72,153,0.4)}}
        .btn-primary:hover{{transform:translateY(-2px);box-shadow:0 12px 35px rgba(236,72,153,0.6)}}
        .btn-follow{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;font-weight:700}}
        .btn-follow.following{{background:rgba(34,197,94,0.2);border:1px solid rgba(34,197,94,0.3);color:#4ade80}}
        .section-title{{font-size:16px;font-weight:700;padding:0 20px;margin-bottom:12px;display:flex;align-items:center;gap:8px}}
        
        /* ═══ فيديوهات محسنة ═══ */
        .videos-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:0 8px 100px}}
        .video-grid-item{{
            aspect-ratio:9/16;position:relative;overflow:hidden;cursor:pointer;
            background:#000;border-radius:6px;transition:all 0.3s;
        }}
        .video-grid-item:hover{{transform:scale(1.03);box-shadow:0 0 20px rgba(236,72,153,0.4);z-index:10}}
        .video-grid-item video,.video-grid-item img{{width:100%;height:100%;object-fit:cover}}
        .video-grid-item .grid-play-icon{{
            position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
            width:40px;height:40px;background:rgba(236,72,153,0.7);
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            font-size:16px;color:#fff;z-index:2;backdrop-filter:blur(10px);
            transition:all 0.3s;opacity:0;
        }}
        .video-grid-item:hover .grid-play-icon{{opacity:1;transform:translate(-50%,-50%) scale(1.2)}}
        .video-grid-item .grid-views{{
            position:absolute;bottom:8px;right:8px;font-size:11px;color:#fff;
            z-index:2;display:flex;align-items:center;gap:3px;
            background:rgba(0,0,0,0.6);padding:4px 8px;border-radius:12px;
            backdrop-filter:blur(10px);
        }}
        .video-grid-item .grid-likes{{
            position:absolute;bottom:8px;left:8px;font-size:11px;color:#ec4899;
            z-index:2;display:flex;align-items:center;gap:3px;
            background:rgba(0,0,0,0.6);padding:4px 8px;border-radius:12px;
            backdrop-filter:blur(10px);
        }}
        .video-grid-item .grid-overlay{{
            position:absolute;inset:0;
            background:linear-gradient(to top,rgba(0,0,0,0.8) 0%,transparent 40%);
            opacity:0;transition:all 0.3s;
        }}
        .video-grid-item:hover .grid-overlay{{opacity:1}}

        /* ═══ نافذة فيديو داخلية ═══ */
        .video-modal{{
            position:fixed;inset:0;background:rgba(0,0,0,0.95);
            z-index:500;display:none;align-items:center;justify-content:center;
            backdrop-filter:blur(20px);
        }}
        .video-modal.show{{display:flex;animation:fadeIn 0.3s ease}}
        @keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
        .video-modal-content{{
            position:relative;max-width:480px;width:100%;max-height:90vh;
            background:rgba(2,6,23,0.98);border-radius:24px;overflow:hidden;
            border:1px solid rgba(236,72,153,0.4);
            box-shadow:0 0 60px rgba(236,72,153,0.3);
            animation:slideUp 0.3s ease;
        }}
        @keyframes slideUp{{from{{transform:translateY(50px);opacity:0}}to{{transform:translateY(0);opacity:1}}}}
        .video-modal-close{{
            position:absolute;top:12px;right:12px;
            background:rgba(0,0,0,0.7);width:40px;height:40px;
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            cursor:pointer;z-index:10;border:1px solid var(--border);
            color:#fff;font-size:18px;transition:all 0.3s;
        }}
        .video-modal-close:hover{{background:var(--accent);transform:rotate(90deg)}}
        .video-modal video{{width:100%;max-height:60vh;background:#000}}
        .video-modal-info{{padding:20px}}
        .video-modal-title{{font-size:15px;font-weight:700;margin-bottom:10px}}
        .video-modal-actions{{display:flex;gap:15px;margin-top:15px;flex-wrap:wrap}}
        .video-action-btn{{
            display:flex;align-items:center;gap:8px;cursor:pointer;
            transition:all 0.3s;font-size:14px;color:var(--text-secondary);
            background:none;border:1px solid var(--border);padding:10px 18px;
            border-radius:25px;
        }}
        .video-action-btn:hover{{
            background:rgba(236,72,153,0.15);color:var(--accent2);
            border-color:var(--accent);transform:translateY(-2px);
            box-shadow:0 0 20px rgba(236,72,153,0.2);
        }}
        .video-action-btn.liked{{
            background:rgba(236,72,153,0.2);color:var(--accent);
            border-color:var(--accent);
        }}

        .empty-state{{text-align:center;opacity:0.5;padding:40px 20px}}
        .empty-state i{{font-size:48px;color:var(--accent);margin-bottom:12px;display:block}}
        .badge-verified{{background:linear-gradient(135deg,#ec4899,#f472b6);color:#fff;font-size:12px;padding:3px 6px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;font-weight:bold;box-shadow:0 0 15px rgba(244,114,182,0.6);animation:verifyPinkGlow 2s ease-in-out infinite}}
        @keyframes verifyPinkGlow{{0%,100%{{box-shadow:0 0 15px rgba(244,114,182,0.6)}}50%{{box-shadow:0 0 25px rgba(244,114,182,0.9)}}}}
        .edit-panel{{position:fixed;bottom:0;left:0;right:0;background:rgba(2,6,23,0.98);backdrop-filter:blur(40px);border-top:2px solid var(--accent);border-radius:24px 24px 0 0;padding:24px 20px 40px;z-index:200;transform:translateY(100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);max-height:80vh;overflow-y:auto;box-shadow:0 -10px 40px rgba(236,72,153,0.1)}}
        .edit-panel.show{{transform:translateY(0)}}
        .edit-panel h3{{font-size:18px;font-weight:700;margin-bottom:20px;color:var(--accent2);text-align:center}}
        .edit-panel label{{display:block;font-size:12px;opacity:0.7;margin-bottom:6px;margin-top:14px}}
        .edit-panel input,.edit-panel textarea{{width:100%;padding:12px 16px;border-radius:14px;background:var(--card);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif;transition:border 0.3s}}
        .edit-panel input:focus,.edit-panel textarea:focus{{border-color:var(--accent);box-shadow:0 0 15px rgba(236,72,153,0.15)}}
        .edit-actions{{display:flex;gap:10px;margin-top:20px}}
        .edit-actions button{{flex:1;padding:12px;border-radius:25px;font-weight:700;cursor:pointer;font-size:14px;transition:all 0.3s}}
        .btn-save{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff}}
        .btn-cancel{{background:var(--card);border:1px solid var(--border);color:#fff}}
        .overlay-panel{{position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:150;display:none}}
        .overlay-panel.show{{display:block}}
        
        /* Admin Panel */
        .admin-panel{{padding:20px;margin:0 8px 100px 8px;background:rgba(236,72,153,0.03);border:1px solid var(--border);border-radius:24px}}
        .admin-panel h3{{color:#f472b6;font-size:20px;margin-bottom:20px;display:flex;align-items:center;gap:10px;font-weight:700}}
        .admin-stats-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:24px}}
        .stat-card{{background:rgba(236,72,153,0.06);border:1px solid rgba(236,72,153,0.15);border-radius:16px;padding:16px;display:flex;align-items:center;gap:14px;backdrop-filter:blur(10px);transition:all 0.3s}}
        .stat-card:hover{{background:rgba(236,72,153,0.1);transform:translateY(-2px)}}
        .stat-icon{{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 4px 15px rgba(236,72,153,0.3)}}
        .stat-info h4{{font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:4px;font-weight:500}}
        .stat-info span{{font-size:22px;font-weight:800}}
        .admin-user-item{{display:flex;align-items:center;justify-content:space-between;padding:10px 8px;border-bottom:1px solid rgba(255,255,255,0.03);transition:background 0.2s;border-radius:8px}}
        .admin-user-item:hover{{background:rgba(236,72,153,0.04)}}
        .admin-user-info{{display:flex;align-items:center;gap:12px;flex:1;min-width:0}}
        .admin-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(236,72,153,0.3);flex-shrink:0}}
        .admin-avatar img{{width:100%;height:100%;object-fit:cover}}
        .admin-user-details h4{{font-weight:600;font-size:15px}}
        .admin-user-details p{{font-size:11px;color:rgba(255,255,255,0.4);margin-top:2px}}
        .admin-user-actions{{display:flex;gap:8px;align-items:center;flex-shrink:0}}
        .admin-btn{{border:none;border-radius:20px;padding:8px 16px;font-size:12px;font-weight:700;cursor:pointer;transition:all 0.2s;display:flex;align-items:center;gap:5px}}
        .admin-btn:hover{{transform:translateY(-2px)}}
        .btn-ban{{background:rgba(255,255,255,0.1);color:#fff;border:1px solid rgba(255,255,255,0.1)}}
        .btn-ban:hover{{background:rgba(239,68,68,0.2);border-color:rgba(239,68,68,0.3)}}
        .btn-unban{{background:rgba(34,197,94,0.1);color:#4ade80;border:1px solid rgba(34,197,94,0.2)}}
        .btn-verify{{background:linear-gradient(135deg,#ec4899,#f472b6);color:#fff;box-shadow:0 4px 12px rgba(236,72,153,0.3)}}
        .btn-delete-video{{background:rgba(239,68,68,0.1);color:#f87171;border:1px solid rgba(239,68,68,0.2)}}
        .btn-delete-video:hover{{background:rgba(239,68,68,0.3)}}
    </style>
</head>
<body>

<div class="load-center" id="loader" style="display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)">
    <div class="spinner"></div><span>💗 تحميل الملف...</span>
</div>

<div id="content" style="display:none">
    <div class="cover-section" id="coverSection" onmousemove="parallaxCover(event)">
        <img class="cover-img" id="coverImg" src="" alt="cover" style="display:none">
        <div class="cover-gradient"></div>
        <div class="cover-glow"></div>
        <div class="cover-edit-btn" id="coverEditBtn" onclick="event.stopPropagation();document.getElementById('coverInput').click()" style="display:none">
            <i class="fas fa-camera"></i>
        </div>
    </div>
    <input type="file" id="coverInput" accept="image/*" style="display:none" onchange="uploadCover(this)">
    
    <button class="btn-back" onclick="history.back()"><i class="fas fa-arrow-right"></i></button>
    
    <div class="avatar-wrap">
        <div class="avatar-lg" id="avatarDisplay">
            <img src="" alt="avatar" id="avatarImg">
            <div class="avatar-edit-btn" id="avatarEditBtn" onclick="event.stopPropagation();document.getElementById('avatarInput').click()" style="display:none">
                <i class="fas fa-camera"></i>
            </div>
            <div class="online-dot" id="onlineDot" style="display:none"></div>
        </div>
    </div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">

    <div class="profile-info">
        <div class="username"><span id="nameDisplay"></span></div>
        <div class="bio-text" id="bioDisplay"></div>
        <div class="contact-info" id="contactInfo"></div>
        <div class="last-seen" id="lastSeenDisplay"></div>
    </div>

    <div class="wallet-mini" id="walletMini" onclick="window.location.href='wallet.html'">
        <i class="fas fa-wallet"></i>
        <span>رصيدك: <span id="profileWalletBalance">0</span> د.ع</span>
        <i class="fas fa-chevron-left"></i>
    </div>

    <div class="stats-row">
        <div class="stat-item" onclick="showList('following')"><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div>
        <div class="stat-item" onclick="showList('followers')"><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div>
        <div class="stat-item"><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div>
    </div>

    <div class="action-btns" id="actionsBar"></div>

    <div class="section-title"><i class="fas fa-video" style="color:var(--accent)"></i> الفيديوهات</div>
    <div class="videos-grid" id="videosGrid"></div>
</div>

<!-- ═══ نافذة الفيديو الداخلية ═══ -->
<div class="video-modal" id="videoModal">
    <div class="video-modal-content">
        <div class="video-modal-close" onclick="closeVideoModal()"><i class="fas fa-times"></i></div>
        <video id="modalVideo" controls autoplay loop></video>
        <div class="video-modal-info">
            <div class="video-modal-title" id="modalVideoTitle"></div>
            <div class="video-modal-actions">
                <button class="video-action-btn" id="modalLikeBtn" onclick="likeCurrentVideo()">
                    <i class="fas fa-heart"></i> <span id="modalLikesCount">0</span>
                </button>
                <button class="video-action-btn" onclick="shareCurrentVideo()">
                    <i class="fas fa-share"></i> مشاركة
                </button>
                <button class="video-action-btn" onclick="copyVideoLink()">
                    <i class="fas fa-link"></i> نسخ الرابط
                </button>
            </div>
        </div>
    </div>
</div>

<div class="overlay-panel" id="overlayPanel" onclick="closeEditPanel()"></div>
<div class="edit-panel" id="editPanel">
    <h3>💗 لوحة تعديل الملف الشخصي</h3>
    <label>👤 اسم المستخدم</label>
    <input type="text" id="editUsername" placeholder="اسم المستخدم">
    <label>📝 السيرة الذاتية</label>
    <textarea id="editBio" placeholder="اكتب شيئاً عن نفسك..."></textarea>
    <label>🌐 الموقع الإلكتروني</label>
    <input type="text" id="editWebsite" placeholder="https://example.com" dir="ltr">
    <label>📧 البريد الإلكتروني</label>
    <input type="text" id="editContactEmail" placeholder="example@email.com" dir="ltr">
    <label>🎨 لون الغلاف</label>
    <div id="coverColors" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px"></div>
    <div class="edit-actions">
        <button class="btn-cancel" onclick="closeEditPanel()">إلغاء</button>
        <button class="btn-save" onclick="saveProfile()"><i class="fas fa-save"></i> حفظ التغييرات</button>
    </div>
</div>

<div class="toast-msg" id="toastMsg">✅ تم</div>

<script src="firebase-config.js"></script>
<script>
    let profileUserId = null, currentUser = null, currentUserData = null;
    let allVideos = [], allUsers = {{}}, isOwnProfile = false, _selectedCover = null;
    let currentVideoId = null, currentVideoData = null;

    window.parallaxCover = function(event) {{
        const img = document.getElementById('coverImg');
        if(!img || !img.src || img.style.display === 'none') return;
        const cover = document.getElementById('coverSection');
        const rect = cover.getBoundingClientRect();
        const y = event.clientY - rect.top;
        const percent = (y / rect.height - 0.5) * 0.15;
        img.style.transform = `translateY(${{percent * 100}}px)`;
    }};

    auth.onAuthStateChanged(async u => {{
        if(!u) {{ window.location.href = 'auth.html'; return; }}
        currentUser = u;
        const params = new URLSearchParams(window.location.search);
        profileUserId = params.get('uid') || u.uid;
        isOwnProfile = (profileUserId === u.uid);
        const snap = await db.ref('users/' + u.uid).get();
        if(snap.exists()) currentUserData = {{uid: u.uid, ...snap.val()}};
        await loadAll();
        await loadProfile();
        if(!isOwnProfile) {{
            db.ref('presence/' + profileUserId).on('value', s => {{
                const isOnline = s.val();
                const dot = document.getElementById('onlineDot');
                const lastSeen = document.getElementById('lastSeenDisplay');
                if(dot) dot.style.display = isOnline ? 'block' : 'none';
                if(lastSeen) {{
                    const userData = allUsers[profileUserId];
                    if(userData) lastSeen.innerHTML = isOnline ? '<i class="fas fa-circle" style="color:#22c55e;font-size:8px"></i> نشط الآن' : '<i class="fas fa-clock"></i> آخر ظهور: ' + formatTime(userData.lastSeen);
                }}
            }});
        }}
        document.getElementById('loader').style.display = 'none';
        document.getElementById('content').style.display = 'block';
    }});

    async function loadAll() {{
        const us = await db.ref('users').once('value'); allUsers = us.val() || {{}};
        const vs = await db.ref('videos').once('value'); allVideos = Object.entries(vs.val() || {{}}).map(([k, v]) => ({{id: k, ...v}}));
    }}

    async function loadProfile() {{
        const u = allUsers[profileUserId];
        if(!u) {{ document.getElementById('content').innerHTML = '<div class="empty-state" style="padding-top:100px"><i class="fas fa-user-slash"></i><p>المستخدم غير موجود</p></div>'; return; }}
        const pinkVerifiedBadge = u.isVerified ? '<span class="badge-verified"><i class="fas fa-check"></i></span>' : '';
        document.getElementById('nameDisplay').innerHTML = '@' + (u.username || 'مستخدم') + ' ' + pinkVerifiedBadge;
        document.getElementById('bioDisplay').innerText = u.bio || 'لم تتم إضافة سيرة ذاتية بعد';
        const contactInfo = document.getElementById('contactInfo');
        let contactHTML = '';
        if(u.website) contactHTML += `<a href="${{u.website}}" target="_blank"><i class="fas fa-globe"></i> ${{u.website.replace('https://','').replace('http://','')}}</a>`;
        if(u.contactEmail) contactHTML += `<a href="mailto:${{u.contactEmail}}"><i class="fas fa-envelope"></i> ${{u.contactEmail}}</a>`;
        contactInfo.innerHTML = contactHTML;
        document.getElementById('statFollowing').innerText = Object.keys(u.following || {{}}).length;
        document.getElementById('statFollowers').innerText = Object.keys(u.followers || {{}}).length;
        const uvs = allVideos.filter(v => v.sender === profileUserId);
        document.getElementById('statLikes').innerText = uvs.reduce((s, v) => s + (v.likes || 0), 0);
        
        // Show wallet balance
        document.getElementById('profileWalletBalance').innerText = formatNumber(u.wallet?.balance || 0);
        
        const coverImg = document.getElementById('coverImg');
        if(u.coverImageUrl) {{ coverImg.src = u.coverImageUrl; coverImg.style.display = 'block'; }}
        else {{ document.getElementById('coverSection').style.background = u.coverColor || COVER_COLORS[0]; coverImg.style.display = 'none'; }}
        document.getElementById('avatarImg').src = u.avatarUrl || (DICEBEAR_URL + '?seed=' + profileUserId);
        if(isOwnProfile) {{ document.getElementById('avatarEditBtn').style.display = 'flex'; document.getElementById('coverEditBtn').style.display = 'flex'; document.getElementById('walletMini').style.display = 'flex'; }}
        else {{ document.getElementById('walletMini').style.display = 'none'; }}
        const lastSeen = document.getElementById('lastSeenDisplay');
        if(!isOwnProfile) {{
            const presenceSnap = await db.ref('presence/' + profileUserId).get();
            const isOnline = presenceSnap.val();
            document.getElementById('onlineDot').style.display = isOnline ? 'block' : 'none';
            lastSeen.innerHTML = isOnline ? '<i class="fas fa-circle" style="color:#22c55e;font-size:8px"></i> نشط الآن' : '<i class="fas fa-clock"></i> آخر ظهور: ' + formatTime(u.lastSeen || u.createdAt);
        }}

        const grid = document.getElementById('videosGrid');
        grid.innerHTML = '';
        if(!uvs.length) {{ grid.innerHTML = '<div class="empty-state" style="grid-column:1/-1"><i class="fas fa-video-slash"></i><p>لا توجد فيديوهات</p></div>'; }}
        else {{
            uvs.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0)).forEach(v => {{
                const d = document.createElement('div');
                d.className = 'video-grid-item';
                d.onclick = () => openVideoModal(v.id);
                d.innerHTML = `
                    ${{v.thumbnail ? `<img src="${{v.thumbnail}}" style="width:100%;height:100%;object-fit:cover">` : '<div style="width:100%;height:100%;background:#111;display:flex;align-items:center;justify-content:center"><i class="fas fa-play" style="color:#555;font-size:24px"></i></div>'}}
                    <div class="grid-overlay"></div>
                    <div class="grid-play-icon"><i class="fas fa-play"></i></div>
                    <div class="grid-views"><i class="fas fa-eye" style="color:var(--accent2)"></i> ${{formatNumber(v.views || 0)}}</div>
                    <div class="grid-likes"><i class="fas fa-heart"></i> ${{formatNumber(v.likes || 0)}}</div>
                `;
                grid.appendChild(d);
            }});
        }}

        const actionsBar = document.getElementById('actionsBar');
        if(isOwnProfile) {{
            actionsBar.innerHTML = `<button class="btn btn-primary" onclick="openEditPanel()"><i class="fas fa-edit"></i> تعديل الملف</button><a href="wallet.html" class="btn" style="color:#ec4899"><i class="fas fa-wallet"></i> المحفظة</a><a href="chat.html" class="btn"><i class="fas fa-envelope"></i> الرسائل</a><button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>`;
        }} else {{
            const isFollowing = currentUserData?.following?.[profileUserId];
            actionsBar.innerHTML = `<button class="btn btn-follow ${{isFollowing ? 'following' : ''}}" id="followBtn" onclick="toggleFollowUser()">${{isFollowing ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}}</button><a href="chat.html?uid=${{profileUserId}}" class="btn btn-primary"><i class="fas fa-comment"></i> مراسلة</a><button class="btn" onclick="copyProfile()"><i class="fas fa-copy"></i> نسخ المعلومات</button>`;
        }}
        if(isOwnProfile && ADMIN_EMAILS.includes(currentUser?.email)) {{ loadAdminPanel(); }}
    }}

    /* ═══ وظائف الفيديو الداخلية ═══ */
    async function openVideoModal(videoId) {{
        const video = allVideos.find(v => v.id === videoId);
        if(!video) return;
        currentVideoId = videoId;
        currentVideoData = video;
        
        // زيادة المشاهدات
        const newViews = (video.views || 0) + 1;
        await db.ref('videos/' + videoId + '/views').set(newViews);
        video.views = newViews;
        
        document.getElementById('modalVideo').src = video.url;
        document.getElementById('modalVideoTitle').innerText = video.description || 'بدون وصف';
        document.getElementById('modalLikesCount').innerText = formatNumber(video.likes || 0);
        updateLikeButton();
        document.getElementById('videoModal').classList.add('show');
        
        // تحديث الشبكة
        await loadProfile();
    }}

    function closeVideoModal() {{
        document.getElementById('videoModal').classList.remove('show');
        document.getElementById('modalVideo').pause();
        document.getElementById('modalVideo').src = '';
        currentVideoId = null;
        currentVideoData = null;
    }}

    async function likeCurrentVideo() {{
        if(!currentVideoId || !currentUser) return;
        const likeRef = db.ref('videos/' + currentVideoId + '/likes');
        const userLikeRef = db.ref('videos/' + currentVideoId + '/likedBy/' + currentUser.uid);
        const snap = await userLikeRef.get();
        
        if(snap.exists()) {{
            // إلغاء الإعجاب
            await likeRef.set(Math.max(0, (currentVideoData.likes || 1) - 1));
            await userLikeRef.remove();
            currentVideoData.likes = Math.max(0, (currentVideoData.likes || 1) - 1);
        }} else {{
            // إضافة إعجاب
            await likeRef.set((currentVideoData.likes || 0) + 1);
            await userLikeRef.set(true);
            currentVideoData.likes = (currentVideoData.likes || 0) + 1;
        }}
        
        document.getElementById('modalLikesCount').innerText = formatNumber(currentVideoData.likes);
        updateLikeButton();
        await loadProfile();
    }}

    async function updateLikeButton() {{
        if(!currentVideoId || !currentUser) return;
        const userLikeRef = await db.ref('videos/' + currentVideoId + '/likedBy/' + currentUser.uid).get();
        const btn = document.getElementById('modalLikeBtn');
        if(userLikeRef.exists()) {{
            btn.classList.add('liked');
            btn.querySelector('i').style.color = '#ec4899';
        }} else {{
            btn.classList.remove('liked');
            btn.querySelector('i').style.color = '';
        }}
    }}

    function shareCurrentVideo() {{
        if(!currentVideoData) return;
        const text = `شاهد هذا الفيديو 💗 ${{currentVideoData.description || ''}}`;
        if(navigator.share) {{
            navigator.share({{title: 'MNAENCA', text: text, url: currentVideoData.url}});
        }} else {{
            copyVideoLink();
        }}
    }}

    function copyVideoLink() {{
        if(!currentVideoData) return;
        navigator.clipboard.writeText(currentVideoData.url);
        showToast('✅ تم نسخ رابط الفيديو');
    }}

    /* ═══ باقي الوظائف ═══ */
    function openEditPanel() {{
        const u = allUsers[profileUserId] || currentUserData;
        document.getElementById('editUsername').value = u.username || '';
        document.getElementById('editBio').value = u.bio || '';
        document.getElementById('editWebsite').value = u.website || '';
        document.getElementById('editContactEmail').value = u.contactEmail || '';
        _selectedCover = u.coverColor || COVER_COLORS[0];
        const colorsDiv = document.getElementById('coverColors');
        colorsDiv.innerHTML = COVER_COLORS.map((c, i) => `<div onclick="selectCover('${{c.replace(/'/g, "\\\\'")}}', this)" style="width:40px;height:40px;border-radius:50%;background:${{c}};cursor:pointer;border:3px solid ${{_selectedCover === c ? '#fff' : 'transparent'}};transition:all 0.2s;box-shadow:0 4px 15px rgba(0,0,0,0.3)" title="غلاف ${{i+1}}"></div>`).join('');
        document.getElementById('editPanel').classList.add('show'); document.getElementById('overlayPanel').classList.add('show');
    }}
    function closeEditPanel() {{ document.getElementById('editPanel').classList.remove('show'); document.getElementById('overlayPanel').classList.remove('show'); }}
    function selectCover(color, el) {{ _selectedCover = color; document.getElementById('coverSection').style.background = color; document.getElementById('coverImg').style.display = 'none'; document.querySelectorAll('#coverColors div').forEach(d => d.style.borderColor = 'transparent'); el.style.borderColor = '#fff'; }}
    async function saveProfile() {{
        const username = document.getElementById('editUsername').value.trim();
        const bio = document.getElementById('editBio').value.trim();
        const website = document.getElementById('editWebsite').value.trim();
        const contactEmail = document.getElementById('editContactEmail').value.trim();
        if(!username || username.length < 3) {{ showToast('❌ اسم المستخدم 3 أحرف على الأقل'); return; }}
        const updates = {{username, bio, website, contactEmail}};
        if(_selectedCover) updates.coverColor = _selectedCover;
        try {{ await db.ref('users/' + profileUserId).update(updates); closeEditPanel(); await loadAll(); await loadProfile(); showToast('✅ تم حفظ التغييرات بنجاح'); }} catch(e) {{ showToast('❌ حدث خطأ'); }}
    }}
    async function uploadAvatar(inp) {{
        const file = inp.files[0]; if(!file) return; showToast('⏳ جاري رفع الصورة...');
        const fd = new FormData(); fd.append('file', file); fd.append('upload_preset', UPLOAD_PRESET);
        try {{
            const res = await fetch('https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', {{method: 'POST', body: fd}});
            const data = await res.json();
            if(data.secure_url) {{ await db.ref('users/' + profileUserId).update({{avatarUrl: data.secure_url, hasCustomAvatar: true}}); document.getElementById('avatarImg').src = data.secure_url; showToast('✅ تم تحديث الصورة الشخصية'); }}
        }} catch(e) {{ showToast('❌ خطأ في الرفع'); }} inp.value = '';
    }}
    async function uploadCover(inp) {{
        const file = inp.files[0]; if(!file) return; showToast('⏳ جاري رفع الغلاف...');
        const fd = new FormData(); fd.append('file', file); fd.append('upload_preset', UPLOAD_PRESET);
        try {{
            const res = await fetch('https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', {{method: 'POST', body: fd}});
            const data = await res.json();
            if(data.secure_url) {{ await db.ref('users/' + profileUserId).update({{coverImageUrl: data.secure_url, hasCustomCover: true}}); const coverImg = document.getElementById('coverImg'); coverImg.src = data.secure_url; coverImg.style.display = 'block'; document.getElementById('coverSection').style.background = 'none'; showToast('✅ تم تحديث الغلاف'); }}
        }} catch(e) {{ showToast('❌ خطأ في الرفع'); }} inp.value = '';
    }}
    async function toggleFollowUser() {{
        if(!currentUser || isOwnProfile) return;
        const btn = document.getElementById('followBtn');
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + profileUserId);
        const targetRef = db.ref('users/' + profileUserId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if(snap.exists()) {{ await userRef.remove(); await targetRef.remove(); btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة'; btn.classList.remove('following'); }}
        else {{ await userRef.set(true); await targetRef.set(true); btn.innerHTML = '<i class="fas fa-user-check"></i> متابع'; btn.classList.add('following'); }}
        await loadAll(); await loadProfile();
    }}
    async function copyProfile() {{
        const u = allUsers[profileUserId];
        const text = `👤 @${{u.username || 'مستخدم'}}\\n📝 ${{u.bio || ''}}\\n💗 MNAENCA 2026`;
        try {{ await navigator.clipboard.writeText(text); }} catch(e) {{ const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta); }}
        showToast('✅ تم نسخ معلومات الملف الشخصي');
    }}
    function showList(type) {{
        const u = allUsers[profileUserId];
        const list = type === 'followers' ? (u?.followers || {{}}) : (u?.following || {{}});
        const ids = Object.keys(list);
        if(!ids.length) {{ alert('لا يوجد'); return; }}
        const names = ids.map(id => {{ const user = allUsers[id]; return user ? '@' + user.username : 'مستخدم'; }}).join('\\n');
        alert((type === 'followers' ? 'المتابِعون' : 'المتابَعون') + ':\\n' + names);
    }}
    function showToast(msg) {{ const toast = document.getElementById('toastMsg'); toast.innerText = msg; toast.classList.add('show'); setTimeout(() => toast.classList.remove('show'), 2500); }}
    function formatTime(ts) {{
        if(!ts) return 'غير معروف';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        if(mins < 1) return 'الآن';
        if(mins < 60) return 'منذ ' + mins + ' دقيقة';
        if(hours < 24) return 'منذ ' + hours + ' ساعة';
        if(days < 7) return 'منذ ' + days + ' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }}
    function formatNumber(num) {{ return (num || 0).toLocaleString('ar-IQ'); }}

    async function loadAdminPanel() {{
        const grid = document.getElementById('videosGrid'); if(!grid) return;
        const oldPanel = document.getElementById('adminPanelContainer'); if(oldPanel) oldPanel.remove();
        const adminDiv = document.createElement('div'); adminDiv.id = 'adminPanelContainer'; adminDiv.className = 'admin-panel';
        const totalUsers = Object.keys(allUsers).length;
        const totalVideos = allVideos.length;
        const totalVerified = Object.values(allUsers).filter(u => u.isVerified).length;
        const totalBanned = Object.values(allUsers).filter(u => u.banned).length;
        adminDiv.innerHTML = `<h3><i class="fas fa-crown"></i> لوحة تحكم الأدمن</h3>
            <div class="admin-stats-grid">
                <div class="stat-card"><div class="stat-icon"><i class="fas fa-users"></i></div><div class="stat-info"><h4>المستخدمين</h4><span>${{totalUsers}}</span></div></div>
                <div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#f59e0b,#ec4899)"><i class="fas fa-video"></i></div><div class="stat-info"><h4>فيديوهات</h4><span>${{totalVideos}}</span></div></div>
                <div class="stat-card"><div class="stat-icon"><i class="fas fa-check-circle"></i></div><div class="stat-info"><h4>موثقين</h4><span>${{totalVerified}}</span></div></div>
                <div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#ef4444,#dc2626)"><i class="fas fa-ban"></i></div><div class="stat-info"><h4>محظورين</h4><span>${{totalBanned}}</span></div></div>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(236,72,153,0.1);padding-bottom:8px">
                <span>📋 قائمة المستخدمين</span><span style="font-size:11px">${{totalUsers}} إجمالي</span>
            </div>
            <div id="adminDynamicList"></div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(236,72,153,0.1);padding-bottom:8px">
                <span>🎬 جميع الفيديوهات</span><span style="font-size:11px">${{totalVideos}} إجمالي</span>
            </div>
            <div id="adminVideosList"></div>`;
        grid.after(adminDiv);
        loadAdminUsersList(); loadAdminVideosList();
    }}

    function loadAdminUsersList() {{
        const listContainer = document.getElementById('adminDynamicList'); if(!listContainer) return;
        const usersArray = Object.entries(allUsers).sort(([, a], [, b]) => (b.createdAt || 0) - (a.createdAt || 0)).slice(0, 15);
        if(!usersArray.length) {{ listContainer.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا يوجد مستخدمون</div>'; return; }}
        listContainer.innerHTML = usersArray.map(([id, u]) => {{
            const avatar = u.avatarUrl || (DICEBEAR_URL + '?seed=' + id);
            const isVerified = u.isVerified;
            const isBanned = u.banned;
            const verifiedBadgeHtml = isVerified ? '<span class="badge-verified"><i class="fas fa-check"></i></span>' : '';
            let actionBtns = '';
            if(isBanned) {{ actionBtns = `<button class="admin-btn btn-unban" onclick="toggleBanUser('${{id}}')"><i class="fas fa-undo"></i> إلغاء الحظر</button>`; }}
            else {{ actionBtns = `<button class="admin-btn btn-verify ${{isVerified ? 'unverify' : ''}}" onclick="toggleVerifyUser('${{id}}')">${{isVerified ? '<i class="fas fa-times-circle"></i> إلغاء' : '<i class="fas fa-check-circle"></i> توثيق'}}</button><button class="admin-btn btn-ban" onclick="toggleBanUser('${{id}}')"><i class="fas fa-ban"></i> حظر</button>`; }}
            return `<div class="admin-user-item"><div class="admin-user-info" onclick="openUserProfile('${{id}}')" style="cursor:pointer"><div class="admin-avatar"><img src="${{avatar}}"></div><div class="admin-user-details"><h4>@${{u.username || 'مستخدم'}} ${{verifiedBadgeHtml}}</h4><p>${{u.email || ''}}</p></div></div><div class="admin-user-actions">${{actionBtns}}</div></div>`;
        }}).join('');
    }}

    function loadAdminVideosList() {{
        const listContainer = document.getElementById('adminVideosList'); if(!listContainer) return;
        const videosArray = allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0)).slice(0, 20);
        if(!videosArray.length) {{ listContainer.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا توجد فيديوهات</div>'; return; }}
        listContainer.innerHTML = videosArray.map(v => {{
            const user = allUsers[v.sender] || {{username: v.senderName || 'مستخدم'}};
            const desc = (v.description || 'بدون وصف').substring(0, 40);
            return `<div class="admin-user-item"><div class="admin-user-info"><div class="admin-avatar" style="border-radius:8px;width:50px;height:70px">${{v.thumbnail ? `<img src="${{v.thumbnail}}" style="object-fit:cover">` : ''}}</div><div class="admin-user-details"><p style="font-size:12px">${{desc}}</p><span style="font-size:10px;opacity:0.4">@${{user.username}} · ❤️ ${{formatNumber(v.likes || 0)}} · 👁️ ${{formatNumber(v.views || 0)}}</span></div></div><div class="admin-user-actions"><button class="admin-btn btn-delete-video" onclick="deleteVideo('${{v.id}}')"><i class="fas fa-trash"></i> حذف</button></div></div>`;
        }}).join('');
    }}

    window.deleteVideo = async function(videoId) {{ if(!confirm('هل أنت متأكد من حذف هذا الفيديو؟')) return; try {{ await db.ref('videos/' + videoId).remove(); showToast('🗑️ تم حذف الفيديو بنجاح'); await loadAll(); await loadProfile(); loadAdminVideosList(); }} catch(e) {{ showToast('❌ فشل حذف الفيديو'); }} }};
    window.toggleVerifyUser = async function(id) {{ const snap = await db.ref('users/' + id).once('value'); const data = snap.val(); if(!data) return; const newState = !data.isVerified; if(!confirm(`تأكيد ${{newState ? 'توثيق' : 'إلغاء توثيق'}} @${{data.username || 'المستخدم'}}؟`)) return; await db.ref('users/' + id).update({{isVerified: newState, verifiedAt: newState ? Date.now() : null, verifiedBy: newState ? currentUser.uid : null}}); await loadAll(); await loadProfile(); showToast(`✅ تم ${{newState ? 'توثيق' : 'إلغاء توثيق'}} المستخدم`); loadAdminUsersList(); }};
    window.toggleBanUser = async function(id) {{ const snap = await db.ref('users/' + id).once('value'); const data = snap.val(); if(!data) return; const newState = !data.banned; if(!confirm(`تأكيد ${{newState ? 'حظر' : 'إلغاء حظر'}} @${{data.username || 'المستخدم'}}؟`)) return; await db.ref('users/' + id).update({{banned: newState, bannedAt: newState ? Date.now() : null, bannedBy: newState ? currentUser.uid : null}}); await loadAll(); await loadProfile(); showToast(`✅ تم ${{newState ? 'حظر' : 'إلغاء حظر'}} المستخدم`); loadAdminUsersList(); }};
    window.openUserProfile = function(id) {{ if(id === currentUser?.uid) window.location.href = 'profile.html'; else window.location.href = 'profile.html?uid=' + id; }};

    console.log('💗 MNAENCA Profile Ready ✨');
</script>
</body>
</html>"""
# ═══════════════════════════════════════════════════════════
# ☁️ 6. upload.html - رفع فيديو مطور (بدون ذكر المبالغ)
# ═══════════════════════════════════════════════════════════

def build_upload():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | رفع فيديو</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto;background:linear-gradient(180deg,#0a0118 0%,#1a0a2e 50%,#0a0118 100%)}}
        
        .header{{
            display:flex;align-items:center;gap:12px;padding:16px 20px;
            border-bottom:1px solid var(--border);
            background:rgba(2,6,23,0.9);backdrop-filter:blur(30px);
            position:sticky;top:0;z-index:100;
            box-shadow:0 4px 30px rgba(0,0,0,0.3);
        }}
        .header h2{{
            font-size:18px;font-weight:800;
            background:linear-gradient(135deg,#ec4899,#f472b6);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            background-clip:text;display:flex;align-items:center;gap:8px;
        }}
        .btn-back{{
            background:rgba(236,72,153,0.1);border:1px solid var(--border);
            width:40px;height:40px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            color:#fff;cursor:pointer;font-size:16px;text-decoration:none;
            transition:all 0.3s;
        }}
        .btn-back:hover{{
            background:rgba(236,72,153,0.3);transform:scale(1.1);
            box-shadow:0 0 20px rgba(236,72,153,0.4);
        }}
        
        .container{{max-width:500px;margin:0 auto;padding:20px}}
        
        /* ═══ بطاقة تحفيزية ═══ */
        .upload-banner{{
            background:linear-gradient(135deg,rgba(236,72,153,0.15),rgba(244,114,182,0.05));
            border:1px solid rgba(236,72,153,0.4);
            border-radius:20px;padding:20px;text-align:center;margin-bottom:24px;
            position:relative;overflow:hidden;
            animation:bannerGlow 3s ease-in-out infinite;
        }}
        @keyframes bannerGlow{{
            0%,100%{{box-shadow:0 0 30px rgba(236,72,153,0.2)}}
            50%{{box-shadow:0 0 50px rgba(236,72,153,0.4)}}
        }}
        .upload-banner::before{{
            content:'';position:absolute;inset:0;
            background:linear-gradient(90deg,transparent,rgba(236,72,153,0.3),transparent);
            animation:shimmer 3s infinite;
        }}
        @keyframes shimmer{{
            0%{{transform:translateX(-100%)}}
            100%{{transform:translateX(100%)}}
        }}
        .upload-banner i{{
            font-size:40px;color:var(--accent2);
            animation:float 2s ease-in-out infinite;
            position:relative;z-index:2;
        }}
        @keyframes float{{
            0%,100%{{transform:translateY(0)}}
            50%{{transform:translateY(-10px)}}
        }}
        .upload-banner h3{{
            font-size:16px;font-weight:800;color:var(--accent2);
            margin-top:12px;position:relative;z-index:2;
        }}
        .upload-banner p{{
            font-size:13px;color:var(--text-secondary);
            margin-top:6px;position:relative;z-index:2;
            line-height:1.6;
        }}
        
        /* ═══ منطقة السحب والإفلات ═══ */
        .dropzone{{
            border:2px dashed rgba(236,72,153,0.4);
            border-radius:24px;padding:50px 20px;text-align:center;
            cursor:pointer;background:rgba(236,72,153,0.03);
            margin-bottom:24px;transition:all 0.4s;
            position:relative;overflow:hidden;
        }}
        .dropzone:hover{{
            border-color:var(--accent);
            background:rgba(236,72,153,0.08);
            box-shadow:0 0 40px rgba(236,72,153,0.2);
            transform:scale(1.01);
        }}
        .dropzone.dragover{{
            border-color:var(--accent);
            background:rgba(236,72,153,0.15);
            box-shadow:0 0 60px rgba(236,72,153,0.4);
            transform:scale(1.03);
        }}
        .dropzone i{{
            font-size:56px;color:var(--accent);
            animation:uploadPulse 2s ease-in-out infinite;
        }}
        @keyframes uploadPulse{{
            0%,100%{{transform:scale(1);opacity:1}}
            50%{{transform:scale(1.1);opacity:0.8}}
        }}
        .dropzone .upload-text{{
            font-size:16px;font-weight:700;margin-top:16px;color:#fff;
        }}
        .dropzone .upload-hint{{
            font-size:12px;opacity:0.5;margin-top:8px;
            display:flex;align-items:center;justify-content:center;gap:8px;
        }}
        .dropzone .upload-hint span{{
            background:rgba(236,72,153,0.1);padding:4px 12px;
            border-radius:12px;border:1px solid var(--border);
        }}
        .dropzone video{{
            width:100%;max-height:250px;object-fit:contain;
            margin-top:16px;border-radius:16px;display:none;
            box-shadow:0 8px 30px rgba(0,0,0,0.4);
        }}
        .dropzone .change-video-btn{{
            display:none;margin-top:12px;
            background:rgba(236,72,153,0.2);border:1px solid var(--accent);
            padding:8px 20px;border-radius:20px;color:var(--accent2);
            font-size:12px;cursor:pointer;font-weight:600;
            transition:all 0.3s;
        }}
        .dropzone .change-video-btn:hover{{
            background:rgba(236,72,153,0.3);
        }}
        
        /* ═══ نموذج البيانات ═══ */
        .form-card{{
            background:rgba(236,72,153,0.03);
            border:1px solid var(--border);
            border-radius:24px;padding:24px;
            backdrop-filter:blur(20px);
            box-shadow:0 8px 32px rgba(0,0,0,0.2);
        }}
        .form-card label{{
            display:flex;align-items:center;gap:8px;
            font-size:13px;font-weight:600;color:var(--text-secondary);
            margin-bottom:8px;margin-top:16px;
        }}
        .form-card label i{{
            color:var(--accent);font-size:14px;
        }}
        .form-card textarea,.form-card input{{
            width:100%;padding:14px 16px;border-radius:16px;
            background:rgba(236,72,153,0.04);
            border:1px solid var(--border);color:#fff;
            font-size:14px;outline:none;resize:none;
            font-family:'Segoe UI',sans-serif;
            transition:all 0.3s;
        }}
        .form-card textarea:focus,.form-card input:focus{{
            border-color:var(--accent);
            box-shadow:0 0 20px rgba(236,72,153,0.15);
            background:rgba(236,72,153,0.06);
        }}
        .form-card textarea{{
            min-height:100px;
        }}
        .char-count{{
            font-size:11px;color:var(--text-muted);
            text-align:left;margin-top:4px;
        }}
        
        /* ═══ شريط التقدم ═══ */
        .progress-wrap{{
            display:none;margin:20px 0;
        }}
        .progress-bar{{
            background:rgba(255,255,255,0.1);
            border-radius:30px;height:8px;overflow:hidden;
            position:relative;
        }}
        .progress-fill{{
            background:linear-gradient(90deg,var(--accent),var(--accent2));
            height:100%;border-radius:30px;width:0%;
            transition:width 0.3s ease;
            position:relative;
        }}
        .progress-fill::after{{
            content:'';position:absolute;inset:0;
            background:linear-gradient(90deg,transparent,rgba(255,255,255,0.5),transparent);
            animation:shimmer 1.5s infinite;
        }}
        .progress-text{{
            text-align:center;font-size:13px;margin-top:8px;
            color:var(--accent2);font-weight:700;
        }}
        
        /* ═══ زر الرفع ═══ */
        .btn-upload{{
            width:100%;padding:16px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;border-radius:30px;color:#fff;
            font-weight:800;font-size:16px;cursor:pointer;
            margin-top:20px;box-shadow:0 10px 30px rgba(236,72,153,0.4);
            transition:all 0.4s;display:flex;align-items:center;
            justify-content:center;gap:10px;
            position:relative;overflow:hidden;
        }}
        .btn-upload::before{{
            content:'';position:absolute;inset:0;
            background:linear-gradient(90deg,transparent,rgba(255,255,255,0.3),transparent);
            animation:shimmer 2s infinite;
        }}
        .btn-upload:hover{{
            transform:translateY(-3px);
            box-shadow:0 15px 40px rgba(236,72,153,0.6);
        }}
        .btn-upload:active{{
            transform:translateY(0);
        }}
        .btn-upload:disabled{{
            opacity:0.5;cursor:not-allowed;transform:none;
        }}
        .btn-upload i{{
            position:relative;z-index:2;
        }}
        .btn-upload span{{
            position:relative;z-index:2;
        }}
        
        /* ═══ حالة الرفع ═══ */
        .status{{
            text-align:center;margin-top:16px;font-size:14px;
            font-weight:600;min-height:24px;
            display:flex;align-items:center;justify-content:center;gap:8px;
        }}
        .status.success{{
            color:#4ade80;
        }}
        .status.error{{
            color:#f87171;
        }}
        .status.loading{{
            color:var(--accent2);
        }}
        .status i{{
            animation:spin 1s linear infinite;
        }}
        @keyframes spin{{
            to{{transform:rotate(360deg)}}
        }}
        
        /* ═══ تأثيرات إضافية ═══ */
        .upload-success-animation{{
            display:none;text-align:center;padding:40px 20px;
        }}
        .upload-success-animation.show{{
            display:block;animation:fadeIn 0.5s ease;
        }}
        .upload-success-animation i{{
            font-size:80px;color:#4ade80;
            animation:successBounce 0.6s ease;
        }}
        @keyframes successBounce{{
            0%{{transform:scale(0)}}
            50%{{transform:scale(1.2)}}
            100%{{transform:scale(1)}}
        }}
        
        @media (max-width:480px){{
            .container{{padding:12px}}
            .dropzone{{padding:30px 16px}}
            .form-card{{padding:18px}}
        }}
    </style>
</head>
<body>

<div class="header">
    <a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a>
    <h2><i class="fas fa-cloud-upload-alt"></i> رفع فيديو جديد</h2>
</div>

<div class="container">
    <!-- ═══ بطاقة تحفيزية ═══ -->
    <div class="upload-banner">
        <i class="fas fa-rocket"></i>
        <h3>🎬 شارك إبداعك مع العالم!</h3>
        <p>ارفع فيديوهاتك واكسب المشاهدات والإعجابات<br>كل فيديو ترفعه يزيد من شهرتك 💗</p>
    </div>

    <!-- ═══ منطقة السحب والإفلات ═══ -->
    <div class="dropzone" id="dropzone" onclick="document.getElementById('videoFile').click()">
        <i class="fas fa-cloud-upload-alt"></i>
        <div class="upload-text">اضغط لاختيار فيديو أو اسحبه هنا</div>
        <div class="upload-hint">
            <span><i class="fas fa-video"></i> MP4</span>
            <span><i class="fas fa-weight"></i> حتى 100MB</span>
            <span><i class="fas fa-clock"></i> أي مدة</span>
        </div>
        <video id="preview" controls></video>
        <button class="change-video-btn" id="changeVideoBtn" onclick="event.stopPropagation();document.getElementById('videoFile').click()">
            <i class="fas fa-sync"></i> تغيير الفيديو
        </button>
    </div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">

    <!-- ═══ نموذج البيانات ═══ -->
    <div class="form-card">
        <label><i class="fas fa-pen"></i> وصف الفيديو</label>
        <textarea id="vidDesc" placeholder="اكتب وصفاً جذاباً... #هاشتاقات" maxlength="150"></textarea>
        <div class="char-count"><span id="charCount">0</span>/150</div>
        
        <label><i class="fas fa-music"></i> الموسيقى</label>
        <input type="text" id="vidMusic" placeholder="Original Sound">
        
        <label><i class="fas fa-tag"></i> التصنيف</label>
        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">
            <div class="category-tag" onclick="selectCategory(this)" data-category="عام">🎬 عام</div>
            <div class="category-tag" onclick="selectCategory(this)" data-category="موسيقى">🎵 موسيقى</div>
            <div class="category-tag" onclick="selectCategory(this)" data-category="كوميدي">😂 كوميدي</div>
            <div class="category-tag" onclick="selectCategory(this)" data-category="تعليمي">📚 تعليمي</div>
            <div class="category-tag" onclick="selectCategory(this)" data-category="رياضة">⚽ رياضة</div>
            <div class="category-tag" onclick="selectCategory(this)" data-category="ألعاب">🎮 ألعاب</div>
        </div>
        
        <!-- ═══ شريط التقدم ═══ -->
        <div class="progress-wrap" id="progressWrap">
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
            </div>
            <div class="progress-text" id="progressText">0%</div>
        </div>
        
        <!-- ═══ زر الرفع ═══ -->
        <button class="btn-upload" id="uploadBtn" onclick="upload()">
            <i class="fas fa-heart"></i>
            <span>رفع الفيديو</span>
        </button>
        
        <!-- ═══ حالة الرفع ═══ -->
        <div class="status" id="status"></div>
    </div>
    
    <!-- ═══ نجاح الرفع ═══ -->
    <div class="upload-success-animation" id="successAnimation">
        <i class="fas fa-check-circle"></i>
        <h3 style="font-size:22px;font-weight:800;margin-top:20px;color:#4ade80">تم الرفع بنجاح!</h3>
        <p style="color:var(--text-secondary);margin-top:10px">سيتم توجيهك للصفحة الرئيسية...</p>
    </div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null, currentUserData = null;
    let selectedFile = null, selectedCategory = 'عام';

    auth.onAuthStateChanged(async u => {{
        if(!u) {{ window.location.href = 'auth.html'; return; }}
        currentUser = u;
        const snap = await db.ref('users/' + u.uid).get();
        if(snap.exists()) currentUserData = {{uid: u.uid, ...snap.val()}};
    }});

    // ═══ اختيار التصنيف ═══
    window.selectCategory = function(el) {{
        document.querySelectorAll('.category-tag').forEach(tag => {{
            tag.style.background = 'rgba(236,72,153,0.05)';
            tag.style.borderColor = 'var(--border)';
            tag.style.color = 'var(--text-secondary)';
        }});
        el.style.background = 'rgba(236,72,153,0.2)';
        el.style.borderColor = 'var(--accent)';
        el.style.color = 'var(--accent2)';
        selectedCategory = el.dataset.category;
    }};

    // ═══ عداد الأحرف ═══
    document.getElementById('vidDesc').addEventListener('input', function() {{
        document.getElementById('charCount').innerText = this.value.length;
    }});

    // ═══ سحب وإفلات ═══
    const dropzone = document.getElementById('dropzone');
    dropzone.addEventListener('dragover', (e) => {{
        e.preventDefault();
        dropzone.classList.add('dragover');
    }});
    dropzone.addEventListener('dragleave', () => {{
        dropzone.classList.remove('dragover');
    }});
    dropzone.addEventListener('drop', (e) => {{
        e.preventDefault();
        dropzone.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if(files.length > 0) {{
            handleFile(files[0]);
        }}
    }});

    // ═══ اختيار الملف ═══
    function onFilePick(inp) {{
        const f = inp.files[0];
        if(!f) return;
        handleFile(f);
        inp.value = '';
    }}

    function handleFile(f) {{
        if(!f.type.startsWith('video/')) {{
            showStatus('❌ اختر ملف فيديو صحيح', 'error');
            return;
        }}
        if(f.size > 100 * 1024 * 1024) {{
            showStatus('❌ حجم الملف كبير - الحد الأقصى 100MB', 'error');
            return;
        }}
        selectedFile = f;
        const reader = new FileReader();
        reader.onload = e => {{
            const video = document.getElementById('preview');
            video.src = e.target.result;
            video.style.display = 'block';
            document.getElementById('changeVideoBtn').style.display = 'inline-block';
            document.querySelector('.upload-text').style.display = 'none';
            document.querySelector('.upload-hint').style.display = 'none';
            showStatus('✅ تم اختيار الفيديو: ' + f.name, 'success');
        }};
        reader.readAsDataURL(f);
    }}

    // ═══ رفع الفيديو ═══
    async function upload() {{
        if(!selectedFile) {{
            showStatus('⚠️ اختر فيديو أولاً', 'error');
            return;
        }}
        if(!currentUser) {{
            showStatus('⚠️ سجل دخول أولاً', 'error');
            return;
        }}

        const desc = document.getElementById('vidDesc').value.trim();
        const music = document.getElementById('vidMusic').value.trim() || 'Original Sound';
        
        // إظهار شريط التقدم
        const progressWrap = document.getElementById('progressWrap');
        progressWrap.style.display = 'block';
        const progressFill = document.getElementById('progressFill');
        const progressText = document.getElementById('progressText');
        progressFill.style.width = '0%';
        progressText.innerText = '0%';
        
        const status = document.getElementById('status');
        status.innerHTML = '<i class="fas fa-spinner"></i> جاري الرفع...';
        status.className = 'status loading';
        
        const uploadBtn = document.getElementById('uploadBtn');
        uploadBtn.disabled = true;
        uploadBtn.innerHTML = '<i class="fas fa-spinner"></i><span>جاري الرفع...</span>';

        const fd = new FormData();
        fd.append('file', selectedFile);
        fd.append('upload_preset', UPLOAD_PRESET);
        
        const xhr = new XMLHttpRequest();
        xhr.open('POST', 'https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/video/upload');
        
        xhr.upload.onprogress = e => {{
            if(e.lengthComputable) {{
                const percent = Math.round((e.loaded / e.total) * 100);
                progressFill.style.width = percent + '%';
                progressText.innerText = percent + '%';
            }}
        }};
        
        xhr.onload = async () => {{
            try {{
                const response = JSON.parse(xhr.responseText);
                
                // حفظ بيانات الفيديو
                await db.ref('videos/').push({{
                    url: response.secure_url,
                    thumbnail: response.secure_url.replace('.mp4', '.jpg'),
                    description: desc,
                    music: music,
                    category: selectedCategory,
                    sender: currentUser.uid,
                    senderName: currentUserData?.username || 'مستخدم',
                    likes: 0,
                    likedBy: {{}},
                    comments: {{}},
                    views: 0,
                    timestamp: Date.now()
                }});
                
                // تحديث محفظة المستخدم بدون ذكر المبلغ
                const walletRef = db.ref('users/' + currentUser.uid + '/wallet');
                const walletSnap = await walletRef.get();
                const wallet = walletSnap.val() || {{balance: 0, totalEarned: 0, totalWithdrawn: 0, pendingWithdrawal: 0, totalViews: 0}};
                
                await walletRef.update({{
                    balance: (wallet.balance || 0) + 1000,
                    totalEarned: (wallet.totalEarned || 0) + 1000
                }});
                
                // إضافة معاملة
                await db.ref('transactions/' + currentUser.uid).push({{
                    type: 'bonus',
                    amount: 1000,
                    description: 'مكافأة رفع فيديو 🎬',
                    status: 'completed',
                    timestamp: Date.now()
                }});
                
                // إظهار نجاح الرفع
                status.innerHTML = '';
                status.className = 'status';
                progressWrap.style.display = 'none';
                
                const successAnim = document.getElementById('successAnimation');
                successAnim.classList.add('show');
                document.querySelector('.form-card').style.display = 'none';
                document.querySelector('.dropzone').style.display = 'none';
                document.querySelector('.upload-banner').style.display = 'none';
                
                setTimeout(() => window.location.href = 'index.html', 2500);
                
            }} catch(e) {{
                showStatus('❌ حدث خطأ في الرفع', 'error');
                uploadBtn.disabled = false;
                uploadBtn.innerHTML = '<i class="fas fa-heart"></i><span>رفع الفيديو</span>';
            }}
        }};
        
        xhr.onerror = () => {{
            showStatus('❌ فشل الاتصال بالخادم', 'error');
            uploadBtn.disabled = false;
            uploadBtn.innerHTML = '<i class="fas fa-heart"></i><span>رفع الفيديو</span>';
        }};
        
        xhr.send(fd);
    }}

    // ═══ عرض الحالة ═══
    function showStatus(msg, type) {{
        const status = document.getElementById('status');
        status.innerHTML = msg;
        status.className = 'status ' + type;
        setTimeout(() => {{
            if(status.className.includes('success')) {{
                status.innerHTML = '';
                status.className = 'status';
            }}
        }}, 3000);
    }}

    console.log('💗 MNAENCA Upload Ready ✨');
</script>

<style>
    /* ═══ تصنيفات ═══ */
    .category-tag{{
        background:rgba(236,72,153,0.05);
        border:1px solid var(--border);
        padding:8px 16px;border-radius:20px;
        cursor:pointer;font-size:12px;font-weight:600;
        transition:all 0.3s;color:var(--text-secondary);
        user-select:none;
    }}
    .category-tag:hover{{
        background:rgba(236,72,153,0.15);
        border-color:var(--accent);
        transform:translateY(-2px);
    }}
</style>

</body>
</html>"""
# ═══════════════════════════════════════════════════════════
# ═══════════════════════════════════════════════════════════
# ☁️ 7. chat.html - دردشة مع صور وصوت
# ═══════════════════════════════════════════════════════════

def build_chat():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | دردشة</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{height:100vh;display:flex;flex-direction:column}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(2,6,23,0.8);backdrop-filter:blur(20px)}}
        .btn-back{{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}
        .msgs{{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}}
        .bubble{{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px;position:relative;animation:msgIn 0.3s ease}}
        @keyframes msgIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
        .bubble.sent{{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end;color:#fff}}
        .bubble.received{{background:rgba(236,72,153,0.06);align-self:flex-start;border:1px solid rgba(236,72,153,0.1)}}
        .bubble img{{max-width:200px;border-radius:12px;cursor:pointer;margin-top:4px;display:block}}
        .bubble audio{{max-width:200px;margin-top:4px}}
        .bubble .time{{font-size:9px;opacity:0.6;margin-top:4px}}
        .input-bar{{display:flex;gap:10px;padding:12px;background:rgba(2,6,23,0.95);backdrop-filter:blur(20px);border-top:1px solid var(--border);align-items:center}}
        .input-bar input{{flex:1;padding:12px 16px;border-radius:30px;background:var(--glass);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}}
        .btn-icon{{width:42px;height:42px;background:rgba(236,72,153,0.1);border:1px solid var(--border);border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;transition:all 0.3s}}
        .btn-icon:hover{{background:rgba(236,72,153,0.25)}}
        .btn-send{{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center}}
        .conv-item{{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer}}
        .conv-item:hover{{background:rgba(236,72,153,0.04)}}
        .chat-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(236,72,153,0.3);flex-shrink:0}}
        .chat-avatar img{{width:100%;height:100%;object-fit:cover}}
        .online-indicator{{width:10px;height:10px;background:#22c55e;border-radius:50%;display:inline-block;margin-left:6px}}
        .image-upload-progress{{
            position:fixed;bottom:100px;left:50%;transform:translateX(-50%);
            background:rgba(2,6,23,0.95);padding:16px 24px;border-radius:20px;
            border:1px solid var(--accent);z-index:1000;text-align:center;
            display:none;
        }}
        .recording-indicator{{
            position:fixed;bottom:100px;left:50%;transform:translateX(-50%);
            background:rgba(2,6,23,0.95);padding:16px 24px;border-radius:20px;
            border:1px solid #ef4444;z-index:1000;text-align:center;
            display:none;color:#ef4444;font-weight:700;
        }}
        .recording-indicator .rec-dot{{
            width:12px;height:12px;background:#ef4444;border-radius:50%;
            display:inline-block;animation:pulse 1s infinite;
        }}
    </style>
</head>
<body>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px"><div class="spinner"></div><span>💗 تحميل...</span></div>

<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header">
        <a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a>
        <h2><i class="fas fa-comments"></i> المحادثات</h2>
    </div>
    <div id="convList" style="flex:1;overflow-y:auto"></div>
</div>

<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header">
        <button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button>
        <div class="chat-avatar" id="chatAvatar"></div>
        <h3 id="chatName">محادثة</h3>
        <span id="chatOnline" style="font-size:11px;opacity:0.5;margin-right:8px"></span>
    </div>
    <div class="msgs" id="msgsList"></div>
    <div class="input-bar">
        <button class="btn-icon" onclick="sendImage()" title="إرسال صورة"><i class="fas fa-image"></i></button>
        <button class="btn-icon" id="btnRecord" onclick="toggleRecording()" title="تسجيل صوتي"><i class="fas fa-microphone"></i></button>
        <input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()">
        <button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button>
        <button class="btn-icon" onclick="copyChat()" title="نسخ المحادثة"><i class="fas fa-copy"></i></button>
    </div>
</div>

<div class="image-upload-progress" id="imageUploadProgress">
    <div class="spinner" style="margin:0 auto 10px"></div>
    <span>⏳ جاري رفع الصورة...</span>
</div>

<div class="recording-indicator" id="recordingIndicator">
    <span class="rec-dot"></span> جاري التسجيل... <span id="recordingTime">0:00</span>
</div>

<input type="file" id="imageInput" accept="image/*" style="display:none">

<div class="toast-msg" id="toastMsg">✅ تم</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser=null, allUsers={{}}, chatUserId=null, messagesListener=null;
    let mediaRecorder=null, audioChunks=[], recordingStartTime=null, recordingTimer=null;
    
    auth.onAuthStateChanged(async u=>{{
        if(!u){{window.location.href='auth.html';return}}
        currentUser=u;
        const us=await db.ref('users').once('value');
        allUsers=us.val()||{{}};
        document.getElementById('loader').style.display='none';
        const params=new URLSearchParams(window.location.search);
        const targetUid=params.get('uid');
        if(targetUid){{openChat(targetUid)}}else{{showConvs()}}
        setInterval(()=>{{if(currentUser)db.ref('users/'+currentUser.uid+'/lastSeen').set(Date.now())}},60000)
    }});
    
    function showConvs(){{
        if(messagesListener){{db.ref('private_messages/'+getChatId()).off('value',messagesListener);messagesListener=null}}
        document.getElementById('chatView').style.display='none';
        document.getElementById('convView').style.display='flex';
        chatUserId=null;
        loadConvs()
    }}
    
    async function loadConvs(){{
        const cl=document.getElementById('convList');
        cl.innerHTML='';
        const snap=await db.ref('private_messages').once('value');
        const all=snap.val()||{{}};
        const found=new Set();
        Object.keys(all).forEach(cid=>{{
            const parts=cid.split('_');
            const u1=parts[0], u2=parts[1];
            const other=u1===currentUser.uid?u2:(u2===currentUser.uid?u1:null);
            if(other&&!found.has(other)&&allUsers[other])found.add(other)
        }});
        if(!found.size){{
            cl.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-comments" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block"></i><p>لا محادثات بعد</p></div>';
            return
        }}
        found.forEach(uid=>{{
            const u=allUsers[uid];
            const d=document.createElement('div');
            d.className='conv-item';
            d.innerHTML=`<div class="chat-avatar"><img src="${{u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}}"></div><div style="flex:1"><div style="font-weight:600">@${{u?.username||'?'}} ${{u?.isVerified?'<span style="color:#f472b6;font-size:12px"><i class="fas fa-check-circle"></i></span>':''}}</div></div><i class="fas fa-chevron-left" style="opacity:0.4;font-size:12px"></i>`;
            d.onclick=()=>openChat(uid);
            cl.appendChild(d)
        }})
    }}
    
    async function openChat(uid){{
        chatUserId=uid;
        const u=allUsers[uid];
        document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');
        document.getElementById('chatAvatar').innerHTML=`<img src="${{u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}}">`;
        document.getElementById('convView').style.display='none';
        document.getElementById('chatView').style.display='flex';
        
        db.ref('presence/'+uid).on('value',s=>{{
            const online=s.val();
            document.getElementById('chatOnline').innerHTML=online?'<span class="online-indicator"></span> نشط الآن':'آخر ظهور: '+formatTime(u?.lastSeen)
        }});
        
        await loadMsgs();
        
        if(messagesListener)db.ref('private_messages/'+getChatId()).off('value',messagesListener);
        messagesListener=db.ref('private_messages/'+getChatId()).on('value',async()=>{{
            await loadMsgs();
        }});
    }}
    
    function getChatId(){{
        return [currentUser.uid,chatUserId].sort().join('_')
    }}
    
    async function loadMsgs(){{
        const ml=document.getElementById('msgsList');
        if(!chatUserId)return;
        const snap=await db.ref('private_messages/'+getChatId()).once('value');
        const ms=snap.val()||{{}};
        ml.innerHTML='';
        const msgsArray=Object.values(ms).sort((a,b)=>(a.timestamp||0)-(b.timestamp||0));
        
        if(!msgsArray.length){{
            ml.innerHTML='<div style="text-align:center;opacity:0.4;padding:40px"><i class="fas fa-comment-dots" style="font-size:40px;color:#ec4899;margin-bottom:10px;display:block"></i><p>ابدأ المحادثة!</p></div>';
            return;
        }}
        
        msgsArray.forEach(m=>{{
            const sent=m.senderId===currentUser.uid;
            const d=document.createElement('div');
            d.className='bubble '+(sent?'sent':'received');
            
            if(m.type==='image' && m.imageUrl){{
                d.innerHTML=`<img src="${{m.imageUrl}}" onclick="window.open('${{m.imageUrl}}','_blank')" alt="صورة"><div class="time">${{new Date(m.timestamp).toLocaleTimeString('ar-SA')}}</div>`;
            }}else if(m.type==='audio' && m.audioUrl){{
                d.innerHTML=`<audio controls src="${{m.audioUrl}}"></audio><div class="time">${{new Date(m.timestamp).toLocaleTimeString('ar-SA')}}</div>`;
            }}else{{
                d.innerHTML=`${{m.text||''}}<div class="time">${{new Date(m.timestamp).toLocaleTimeString('ar-SA')}}</div>`;
            }}
            ml.appendChild(d);
        }});
        ml.scrollTop=ml.scrollHeight;
    }}
    
    async function sendMsg(){{
        const inp=document.getElementById('msgInput');
        const txt=inp.value.trim();
        if(!txt||!chatUserId)return;
        await db.ref('private_messages/'+getChatId()).push({{
            senderId:currentUser.uid,
            text:txt,
            type:'text',
            timestamp:Date.now()
        }});
        inp.value='';
        await loadMsgs();
    }}
    
    function sendImage(){{
        if(!chatUserId)return;
        const inp=document.getElementById('imageInput');
        inp.onchange=async(e)=>{{
            const file=e.target.files[0];
            if(!file)return;
            
            if(file.size>5*1024*1024){{
                showToast('❌ حجم الصورة كبير جداً (الحد الأقصى 5MB)');
                return;
            }}
            
            document.getElementById('imageUploadProgress').style.display='block';
            
            try{{
                const fd=new FormData();
                fd.append('file',file);
                fd.append('upload_preset',UPLOAD_PRESET);
                
                const res=await fetch(CLOUDINARY_IMAGE_UPLOAD_URL,{{
                    method:'POST',
                    body:fd
                }});
                
                const data=await res.json();
                
                if(data.secure_url){{
                    await db.ref('private_messages/'+getChatId()).push({{
                        senderId:currentUser.uid,
                        type:'image',
                        imageUrl:data.secure_url,
                        timestamp:Date.now()
                    }});
                    await loadMsgs();
                    showToast('✅ تم إرسال الصورة');
                }}else{{
                    showToast('❌ فشل رفع الصورة');
                }}
            }}catch(err){{
                console.error('Image upload error:',err);
                showToast('❌ خطأ في رفع الصورة');
            }}finally{{
                document.getElementById('imageUploadProgress').style.display='none';
            }}
        }};
        inp.click();
    }}
    
    // 🎤 Voice Recording Functions
    async function toggleRecording(){{
        if(!chatUserId)return;
        const btn=document.getElementById('btnRecord');
        
        if(mediaRecorder && mediaRecorder.state==='recording'){{
            // Stop recording
            mediaRecorder.stop();
            btn.innerHTML='<i class="fas fa-microphone"></i>';
            btn.style.background='rgba(236,72,153,0.1)';
            document.getElementById('recordingIndicator').style.display='none';
            clearInterval(recordingTimer);
        }}else{{
            // Start recording
            try{{
                const stream=await navigator.mediaDevices.getUserMedia({{audio:true}});
                mediaRecorder=new MediaRecorder(stream);
                audioChunks=[];
                
                mediaRecorder.ondataavailable=e=>{{
                    if(e.data.size>0)audioChunks.push(e.data);
                }};
                
                mediaRecorder.onstop=async()=>{{
                    const audioBlob=new Blob(audioChunks,{{type:'audio/webm'}});
                    stream.getTracks().forEach(track=>track.stop());
                    
                    if(audioBlob.size>0){{
                        document.getElementById('imageUploadProgress').style.display='block';
                        
                        try{{
                            const fd=new FormData();
                            fd.append('file',audioBlob,'voice-message.webm');
                            fd.append('upload_preset',UPLOAD_PRESET);
                            
                            const res=await fetch(CLOUDINARY_AUDIO_UPLOAD_URL,{{
                                method:'POST',
                                body:fd
                            }});
                            
                            const data=await res.json();
                            
                            if(data.secure_url){{
                                await db.ref('private_messages/'+getChatId()).push({{
                                    senderId:currentUser.uid,
                                    type:'audio',
                                    audioUrl:data.secure_url,
                                    timestamp:Date.now()
                                }});
                                await loadMsgs();
                                showToast('✅ تم إرسال الرسالة الصوتية');
                            }}else{{
                                showToast('❌ فشل رفع الصوت');
                            }}
                        }}catch(err){{
                            console.error('Audio upload error:',err);
                            showToast('❌ خطأ في رفع الصوت');
                        }}finally{{
                            document.getElementById('imageUploadProgress').style.display='none';
                        }}
                    }}
                    
                    mediaRecorder=null;
                    audioChunks=[];
                }};
                
                mediaRecorder.start();
                recordingStartTime=Date.now();
                recordingTimer=setInterval(updateRecordingTime,1000);
                
                btn.innerHTML='<i class="fas fa-stop"></i>';
                btn.style.background='rgba(239,68,68,0.3)';
                document.getElementById('recordingIndicator').style.display='block';
                updateRecordingTime();
            }}catch(err){{
                console.error('Recording error:',err);
                showToast('❌ لا يمكن الوصول للميكروفون');
            }}
        }}
    }}
    
    function updateRecordingTime(){{
        if(!recordingStartTime)return;
        const elapsed=Math.floor((Date.now()-recordingStartTime)/1000);
        const mins=Math.floor(elapsed/60);
        const secs=elapsed%60;
        document.getElementById('recordingTime').innerText=mins+':'+(secs<10?'0':'')+secs;
    }}
    
    async function copyChat(){{
        if(!chatUserId)return;
        const snap=await db.ref('private_messages/'+getChatId()).once('value');
        const msgs=snap.val()||{{}};
        let text='💬 محادثة MNAENCA\\n'+'─'.repeat(30)+'\\n';
        Object.values(msgs).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{{
            const sender=m.senderId===currentUser.uid?'أنت':(allUsers[m.senderId]?.username||'مستخدم');
            const content=m.type==='image'?'[صورة 📷]':(m.type==='audio'?'[رسالة صوتية 🎤]':m.text);
            const time=new Date(m.timestamp).toLocaleTimeString('ar-SA');
            text+=`\\n${{sender}} (${{time}}):\\n${{content}}\\n`;
        }});
        try{{await navigator.clipboard.writeText(text)}}catch(e){{
            const ta=document.createElement('textarea');
            ta.value=text;
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
        }}
        showToast('✅ تم نسخ المحادثة');
    }}
    
    function showToast(msg){{
        const toast=document.getElementById('toastMsg');
        toast.innerText=msg;
        toast.classList.add('show');
        setTimeout(()=>toast.classList.remove('show'),2500);
    }}
    
    function formatTime(ts){{
        if(!ts)return'غير معروف';
        const diff=Date.now()-ts;
        const mins=Math.floor(diff/60000);
        const hours=Math.floor(diff/3600000);
        const days=Math.floor(diff/86400000);
        if(mins<1)return'الآن';
        if(mins<60)return'منذ '+mins+' دقيقة';
        if(hours<24)return'منذ '+hours+' ساعة';
        if(days<7)return'منذ '+days+' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }}
    
    console.log('💗 MNAENCA Chat Ready with Image & Voice Support');
</script>
</body>
</html>"""
# ═══════════════════════════════════════════════════════════
# ☁️ 8. search.html - صفحة البحث (جديدة)
# ═══════════════════════════════════════════════════════════

def build_search():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | بحث</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}
        .search-box{{
            flex:1;display:flex;align-items:center;gap:8px;
            background:rgba(236,72,153,0.06);border:1px solid var(--border);
            border-radius:30px;padding:8px 16px;
        }}
        .search-box input{{
            flex:1;background:none;border:none;color:#fff;
            font-size:14px;outline:none;
        }}
        .search-box input::placeholder{{color:rgba(255,255,255,0.3)}}
        .results{{padding:16px}}
        .user-result{{
            display:flex;align-items:center;gap:12px;
            padding:14px;border-bottom:1px solid var(--border);
            cursor:pointer;border-radius:12px;transition:background 0.2s;
        }}
        .user-result:hover{{background:rgba(236,72,153,0.04)}}
        .result-avatar{{width:50px;height:50px;border-radius:50%;overflow:hidden;border:2px solid rgba(236,72,153,0.3)}}
        .result-avatar img{{width:100%;height:100%;object-fit:cover}}
        .video-result{{
            display:flex;align-items:center;gap:12px;
            padding:14px;border-bottom:1px solid var(--border);
            cursor:pointer;border-radius:12px;transition:background 0.2s;
        }}
        .video-result:hover{{background:rgba(236,72,153,0.04)}}
        .result-thumb{{width:60px;height:80px;border-radius:8px;overflow:hidden;background:#111}}
        .result-thumb img{{width:100%;height:100%;object-fit:cover}}
    </style>
</head>
<body>
<div class="header">
    <a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a>
    <div class="search-box">
        <i class="fas fa-search" style="color:var(--accent)"></i>
        <input type="text" id="searchInput" placeholder="ابحث عن مستخدمين أو فيديوهات..." onkeyup="handleSearch(this.value)">
    </div>
</div>
<div class="results" id="searchResults">
    <div style="text-align:center;opacity:0.5;padding:40px">
        <i class="fas fa-search" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block"></i>
        <p>ابحث عن مستخدمين أو فيديوهات</p>
    </div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser=null, allUsers={{}}, allVideos=[];
    
    auth.onAuthStateChanged(async u=>{{
        if(!u){{window.location.href='auth.html';return}}
        currentUser=u;
        const us=await db.ref('users').once('value');
        allUsers=us.val()||{{}};
        const vs=await db.ref('videos').once('value');
        allVideos=Object.entries(vs.val()||{{}}).map(([k,v])=>({{id:k,...v}}));
    }});
    
    function handleSearch(query){{
        const results=document.getElementById('searchResults');
        query=query.trim().toLowerCase();
        
        if(!query){{
            results.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-search" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block"></i><p>ابحث عن مستخدمين أو فيديوهات</p></div>';
            return;
        }}
        
        // Search users
        const matchedUsers=Object.entries(allUsers).filter(([id,u])=>
            (u.username||'').toLowerCase().includes(query) ||
            (u.bio||'').toLowerCase().includes(query)
        );
        
        // Search videos
        const matchedVideos=allVideos.filter(v=>
            (v.description||'').toLowerCase().includes(query) ||
            (v.music||'').toLowerCase().includes(query)
        );
        
        let html='';
        
        if(matchedUsers.length){{
            html+='<h3 style="margin:16px 0 8px;color:var(--accent)"><i class="fas fa-users"></i> المستخدمين</h3>';
            matchedUsers.slice(0,10).forEach(([id,u])=>{{
                html+=`<div class="user-result" onclick="openProfile('${{id}}')">
                    <div class="result-avatar"><img src="${{u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}}"></div>
                    <div style="flex:1">
                        <div style="font-weight:600">@${{u.username||'مستخدم'}} ${{u.isVerified?'<span style="color:#f472b6"><i class="fas fa-check-circle"></i></span>':''}}</div>
                        <div style="font-size:12px;opacity:0.5">${{u.bio||''}}</div>
                    </div>
                </div>`;
            }});
        }}
        
        if(matchedVideos.length){{
            html+='<h3 style="margin:16px 0 8px;color:var(--accent)"><i class="fas fa-video"></i> الفيديوهات</h3>';
            matchedVideos.slice(0,10).forEach(v=>{{
                const user=allUsers[v.sender]||{{username:'مستخدم'}};
                html+=`<div class="video-result" onclick="window.open('${{v.url}}','_blank')">
                    <div class="result-thumb">${{v.thumbnail?`<img src="${{v.thumbnail}}">`:''}}</div>
                    <div style="flex:1">
                        <div style="font-size:14px">${{(v.description||'').substring(0,50)}}</div>
                        <div style="font-size:11px;opacity:0.5;margin-top:4px">@${{user.username}} · 👁️ ${{v.views||0}} · ❤️ ${{v.likes||0}}</div>
                    </div>
                </div>`;
            }});
        }}
        
        if(!matchedUsers.length && !matchedVideos.length){{
            html='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-search-minus" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block"></i><p>لا توجد نتائج</p></div>';
        }}
        
        results.innerHTML=html;
    }}
    
    function openProfile(uid){{
        if(uid===currentUser?.uid)window.location.href='profile.html';
        else window.location.href='profile.html?uid='+uid;
    }}
    
    console.log('💗 MNAENCA Search Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 9. notifications.html - إشعارات
# ═══════════════════════════════════════════════════════════

def build_notifications():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | إشعارات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}
        .notif-item{{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center}}
        .notif-icon{{width:40px;height:40px;border-radius:50%;background:rgba(236,72,153,0.1);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--accent);flex-shrink:0}}
    </style>
</head>
<body>
<div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-bell"></i> الإشعارات</h2></div>
<div id="notifsList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;loadNotifs()}});
    async function loadNotifs(){{
        const snap=await db.ref('notifications/'+currentUser.uid).once('value');
        const ns=snap.val()||{{}};
        const c=document.getElementById('notifsList');
        const items=Object.values(ns).reverse();
        if(!items.length){{c.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';return}}
        c.innerHTML=items.map(n=>`<div class="notif-item"><div class="notif-icon"><i class="fas fa-bell"></i></div><div style="flex:1"><div style="font-weight:600">${{n.from||'مستخدم'}}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${{n.msg||''}}</div><div style="font-size:10px;opacity:0.3;margin-top:4px">${{new Date(n.timestamp).toLocaleString('ar-SA')}}</div></div></div>`).join('');
    }}
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 10. settings.html - إعدادات
# ═══════════════════════════════════════════════════════════

def build_settings():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💗 MNAENCA | إعدادات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}
        .setting-item{{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s;text-decoration:none;color:#fff}}
        .setting-item:hover{{background:var(--glass)}}
        .setting-item i{{color:var(--accent);font-size:18px;width:30px}}
        .btn-danger{{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}}
    </style>
</head>
<body>
<div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-cog"></i> الإعدادات</h2></div>
<div style="padding:8px 0">
    <a href="profile.html" class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user"></i><span>تعديل الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></a>
    <a href="wallet.html" class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-wallet" style="color:#ec4899"></i><span>محفظة الأرباح</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></a>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-lock"></i><span>الخصوصية</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-globe"></i><span>اللغة</span></div><span style="opacity:0.5;font-size:13px">العربية</span></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">v2026.4 💗</span></div>
    <button class="btn-danger" onclick="if(confirm('تسجيل الخروج؟')){{auth.signOut();window.location.href='auth.html'}}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
</div>
<script src="firebase-config.js"></script>
<script>auth.onAuthStateChanged(u=>{{if(!u)window.location.href='auth.html'}});</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  💗  MNAENCA 2026 - PINK LUXURY EDITION  ✨              ║
║     Ultimate Generator - 10 Files                           ║
║                                                              ║
║  💬 Comments + Share + Voice Chat + Wallet (Profile)     ║
║  🔥 Firebase: bomk-9f6ec                                  ║
║  ☁️ Cloudinary: vt6hibdu / y66.ko                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING FILES - إنشاء الملفات")
    
    # Clean output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("wallet.html", build_wallet())
    write("profile.html", build_profile())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("search.html", build_search())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())
    
    # Copy to root for GitHub Pages
    for f in os.listdir(OUTPUT_DIR):
        src = os.path.join(OUTPUT_DIR, f)
        dst = os.path.join('.', f)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
    
    print(f"""
{'='*60}
  💗 BUILD COMPLETE! ✨
{'='*60}

  📊 {TOTAL_LINES} سطر - 10 ملفات

  ✨ المميزات:
     • 💰 محفظة أرباح (في الملف الشخصي فقط)
     • 💗 وردي فاخر
     • 👁️ عداد المشاهدات
     • 🔍 بحث بدلاً من استكشاف
     • 💬 دردشة مع صور وصوت
     • 🎤 رسائل صوتية
     • 👤 ملف شخصي محسن
     • 🔔 إشعارات
     • 🗑️ لوحة أدمن

  🔑 Firebase: bomk-9f6ec
  ☁️ Cloudinary: vt6hibdu / y66.ko
  👑 Admin: jasim28v@gmail.com

  💗 READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
