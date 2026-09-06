// ☁️ MNAENCA 2026 - Pink Luxury Configuration
// Firebase: bomk-9f6ec | Cloudinary: vt6hibdu
// ✨ PREMIUM: Comments + Share + Wallet (Profile) + Voice Chat

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
const CLOUDINARY_AUDIO_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/video/upload`;

// ☁️ MNAENCA Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #831843, #be185d, #ec4899)",
    "linear-gradient(135deg, #500724, #831843, #be185d)",
    "linear-gradient(135deg, #9d174d, #db2777, #f472b6)",
    "linear-gradient(135deg, #4a044e, #86198f, #d946ef)",
    "linear-gradient(135deg, #be185d, #f472b6, #fbcfe8)",
    "linear-gradient(135deg, #2d0a1e, #4a0d2e, #be185d)"
];

// 💰 Iraqi Dinar Earnings Settings (Profile Only)
const VIEW_RATE_IQD = 100;
const MIN_WITHDRAWAL_IQD = 10000;
const USD_TO_IQD = 1450;

// ☁️ App Info
const APP_NAME = "MNAENCA";
const APP_VERSION = "2026.4";
const PRIMARY_COLOR = "#ec4899";
const SECONDARY_COLOR = "#f472b6";
const GOLD_COLOR = "#fbbf24";
const WATERMARK_TEXT = "☁️ MNAENCA";
const WATERMARK_URL = "https://res.cloudinary.com/vt6hibdu/image/upload/v1/watermark_mnaenca";

console.log('💗 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #ec4899; font-size: 16px; font-weight: bold;');
console.log('💰 %cEarnings System Active - '+VIEW_RATE_IQD+' IQD/View (Profile Only)', 'color: #ec4899; font-size: 14px; font-weight: bold;');
