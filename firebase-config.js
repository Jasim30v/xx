// 🎀 BOMK 2026 - Pink Luxury Configuration
// Firebase: bomk-9f6ec | Cloudinary: vt6hibdu
// ✨ PREMIUM: Comments + Share + Wallet + Search + Views

const firebaseConfig = {
    apiKey: "AIzaSyAAiH5kBtNBfuRbXddoCuLet9IGMG2U7q0",
    authDomain: "bomk-9f6ec.firebaseapp.com",
    databaseURL: "https://bomk-9f6ec-default-rtdb.firebaseio.com",
    projectId: "bomk-9f6ec",
    storageBucket: "bomk-9f6ec.firebasestorage.app",
    messagingSenderId: "743058000945",
    appId: "1:743058000945:web:a862e1eecf7d3d98925910",
    measurementId: "G-7F4W2H5Z3Y"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "vt6hibdu";
const UPLOAD_PRESET = "y66.ko";
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/auto/upload`;
const CLOUDINARY_IMAGE_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload`;

// 🎀 BOMK Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #4a0025, #800040, #c9184a)",
    "linear-gradient(135deg, #2d0015, #590d22, #a4133c)",
    "linear-gradient(135deg, #3d0020, #6b0035, #c9184a)",
    "linear-gradient(135deg, #1a0010, #4a0025, #800040)",
    "linear-gradient(135deg, #590d22, #a4133c, #ff4d6d)",
    "linear-gradient(135deg, #0a0005, #2d0015, #590d22)"
];

// 💰 Iraqi Dinar Earnings Settings
const VIEW_RATE_IQD = 100;
const MIN_WITHDRAWAL_IQD = 10000;
const USD_TO_IQD = 1450;

// 🎀 App Info
const APP_NAME = "BOMK";
const APP_VERSION = "2026.5";
const PRIMARY_COLOR = "#ff4d6d";
const SECONDARY_COLOR = "#ff8fa3";
const GOLD_COLOR = "#fbbf24";
const WATERMARK_TEXT = "🎀 BOMK";
const WATERMARK_URL = "https://res.cloudinary.com/vt6hibdu/image/upload/v1/watermark_bomk";

console.log('🎀 %c'+APP_NAME+' v'+APP_VERSION+' Ready 💖', 'color: #ff4d6d; font-size: 16px; font-weight: bold;');
console.log('💰 %cEarnings System Active - '+VIEW_RATE_IQD+' IQD/View', 'color: #fbbf24; font-size: 14px; font-weight: bold;');
console.log('👁️ %cViews Counter Active', 'color: #ff8fa3; font-size: 14px; font-weight: bold;');
