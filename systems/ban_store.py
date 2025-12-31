# systems/ban_store.py

from datetime import datetime

# تخزين مؤقت للبانات المؤقتة (هيتربط DB بعدين)
# usn: {admin, reason, release_date, ign}
ban_store = {}

def add_temp_ban(usn: int, admin: str, reason: str, release_date: datetime, ign: str):
    ban_store[usn] = {
        "admin": admin,
        "reason": reason,
        "release_date": release_date,
        "ign": ign
    }

def remove_ban(usn: int):
    if usn in ban_store:
        del ban_store[usn]

def get_ban(usn: int):
    return ban_store.get(usn)

def all_bans():
    return ban_store.items()