import os
import json
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")
FIREBASE_SERVICE_ACCOUNT_JSON = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")

if not BOT_TOKEN or not FIREBASE_DATABASE_URL or not FIREBASE_SERVICE_ACCOUNT_JSON:
    raise ValueError("Missing environment variables. Check your .env file.")

# Инициализация Firebase
try:
    service_account_info = json.loads(FIREBASE_SERVICE_ACCOUNT_JSON)
    cred = credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DATABASE_URL
    })
    print("✅ Firebase initialized successfully")
except Exception as e:
    print(f"❌ Error initializing Firebase: {e}")
    raise
