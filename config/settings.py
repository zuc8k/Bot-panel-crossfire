# config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# DISCORD
# =========================
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN not found in .env")

OWNER_ID = int(os.getenv("OWNER_ID", 0))
if not OWNER_ID:
    raise RuntimeError("❌ OWNER_ID not found in .env")


# =========================
# ADMIN LOGS
# =========================
ADMIN_LOG_CHANNEL_ID = int(os.getenv("ADMIN_LOG_CHANNEL_ID", 0))


# =========================
# ACCESS CONTROL
# =========================
# IDs مسموح لهم يستخدموا البوت (فاضية = الكل)
ALLOWED_IDS = [
    int(x)
    for x in os.getenv("ALLOWED_IDS", "").split(",")
    if x.strip().isdigit()
]

# Channels مسموح فيها الأوامر (فاضية = أي تشانل)
ALLOWED_CHANNELS = [
    int(x)
    for x in os.getenv("ALLOWED_CHANNELS", "").split(",")
    if x.strip().isdigit()
]


# =========================
# DATABASES
# =========================
DATABASES = {
    "CF_SA_GAME": {
        "host": os.getenv("CF_SA_GAME_HOST"),
        "db": os.getenv("CF_SA_GAME_DB"),
        "user": os.getenv("CF_SA_GAME_USER"),
        "password": os.getenv("CF_SA_GAME_PASSWORD"),
    },
    "CF_WEB": {
        "host": os.getenv("CF_WEB_HOST"),
        "db": os.getenv("CF_WEB_DB"),
        "user": os.getenv("CF_WEB_USER"),
        "password": os.getenv("CF_WEB_PASSWORD"),
    },
    "G4BOX_SA_BILL_DB": {
        "host": os.getenv("G4BOX_SA_BILL_DB_HOST"),
        "db": os.getenv("G4BOX_SA_BILL_DB"),
        "user": os.getenv("G4BOX_SA_BILL_DB_USER"),
        "password": os.getenv("G4BOX_SA_BILL_DB_PASSWORD"),
    },
}