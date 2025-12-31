# core/ranks.py

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

# تخزين مؤقت (هيتربط بملف/DB لاحقًا)
user_ranks = {}

def get_user_rank(user_id: int, owner_id: int) -> str:
    if user_id == owner_id:
        return OWNER
    return user_ranks.get(str(user_id), MEMBER)