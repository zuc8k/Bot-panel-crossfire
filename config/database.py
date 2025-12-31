import os
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

if not DB_SERVER or not DB_USER or not DB_PASS:
    raise RuntimeError("❌ Database credentials missing in .env")

DATABASES = {
    "CF_WEB": "CF_WEB",
    "CF_SA_GAME": "CF_SA_GAME",
    "CF_SA_GUILD": "CF_SA_GUILD",
    "G4BOX_SA_BILL_DB": "G4BOX_SA_BILL_DB",
    "CF_SA_LOG": "CF_SA_LOG"
}