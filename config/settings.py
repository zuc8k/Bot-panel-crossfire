import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ DISCORD_TOKEN not found in .env")

OWNER_ID = 559591858519670796

ALLOWED_IDS = [OWNER_ID]

ALLOWED_CHANNELS = []