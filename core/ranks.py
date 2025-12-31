# core/ranks.py

import json
import os
from config.settings import OWNER_ID

RANKS_FILE = "user_ranks.json"

OWNER = "OWNER"
ADMIN = "A"
GUARD = "G"
MEMBER = "M"

RANK_LEVELS = {
    MEMBER: 1,
    GUARD: 2,
    ADMIN: 3,
    OWNER: 4
}

RANK_NAMES = {
    MEMBER: "👤 Member",
    GUARD: "🛡️ Guardian",
    ADMIN: "👑 Admin",
    OWNER: "👑 Owner"
}

user_ranks = {}

def load_ranks():
    global user_ranks
    if os.path.exists(RANKS_FILE):
        with open(RANKS_FILE, "r", encoding="utf-8") as f:
            user_ranks = json.load(f)
    else:
        user_ranks = {str(OWNER_ID): OWNER}
        save_ranks()

def save_ranks():
    with open(RANKS_FILE, "w", encoding="utf-8") as f:
        json.dump(user_ranks, f, indent=4)

def get_user_rank(user_id: int) -> str:
    if user_id == OWNER_ID:
        return OWNER
    return user_ranks.get(str(user_id), MEMBER)

def set_user_rank(user_id: int, rank: str) -> bool:
    if user_id == OWNER_ID:
        return False
    user_ranks[str(user_id)] = rank
    save_ranks()
    return True

def remove_user_rank(user_id: int):
    uid = str(user_id)
    if uid in user_ranks and user_id != OWNER_ID:
        del user_ranks[uid]
        save_ranks()