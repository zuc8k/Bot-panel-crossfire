# core/ranks.py
import json
import os
from config.settings import OWNER_ID

RANKS_FILE = "user_ranks.json"

OWNER = "OWNER"
ADMIN = "A"
GUARD = "G"
MEMBER = "M"

RANK_LEVELS = {MEMBER: 1, GUARD: 2, ADMIN: 3, OWNER: 4}
RANK_NAMES = {
    MEMBER: " Member",
    GUARD: "️ Guardian",
    ADMIN: " Admin",
    OWNER: " Owner",
}

user_ranks: dict[str, str] = {}


def load_ranks() -> None:
    global user_ranks
    try:
        if os.path.exists(RANKS_FILE):
            with open(RANKS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    user_ranks = data
                else:
                    user_ranks = {str(OWNER_ID): OWNER}
                    save_ranks()
        else:
            user_ranks = {str(OWNER_ID): OWNER}
            save_ranks()
    except (json.JSONDecodeError, OSError) as e:
        print(f"❌ Failed to load ranks file: {e}")
        user_ranks = {str(OWNER_ID): OWNER}
        save_ranks()


def save_ranks() -> None:
    try:
        with open(RANKS_FILE, "w", encoding="utf-8") as f:
            json.dump(user_ranks, f, indent=4)
    except OSError as e:
        print(f"❌ Failed to save ranks: {e}")


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


def remove_user_rank(user_id: int) -> None:
    uid = str(user_id)
    if uid in user_ranks and user_id != OWNER_ID:
        del user_ranks[uid]
        save_ranks()