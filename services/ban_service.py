# services/ban_service.py
from datetime import datetime
from database.connection import cursors, connections
from systems.ban_utils import parse_duration
from systems.ban_store import add_temp_ban


# =========================
# BAN PLAYER
# =========================
def ban_player_logic(ign: str, duration: str):
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")
    if not cursor or not conn:
        return None, "DB_ERROR"

    cursor.execute(
        "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK = ?", ign
    )
    row = cursor.fetchone()
    if not row:
        return None, "NOT_FOUND"

    usn, hold_type = row
    if hold_type == "E":
        return None, "ALREADY_BANNED"

    release_date = parse_duration(duration)

    cursor.execute(
        "UPDATE CF_USER SET HOLD_TYPE = 'E' WHERE USN = ?", usn
    )
    conn.commit()

    # تخزين الحظر المؤقت في ban_store ليتمكن auto_unban من رفعه
    if release_date is not None:
        add_temp_ban(
            usn=usn,
            admin="system",  # يمكن تمرير اسم المسؤول من الأمر لاحقًا
            reason="Temporary ban",
            release_date=release_date,
            ign=ign,
        )

    return {
        "usn": usn,
        "nick": ign,
        "duration": duration,
        "release_date": release_date,
    }, "BANNED"


# =========================
# UNBAN PLAYER
# =========================
def unban_player_logic(ign: str):
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")
    if not cursor or not conn:
        return None, "DB_ERROR"

    cursor.execute(
        "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK = ?", ign
    )
    row = cursor.fetchone()
    if not row:
        return None, "NOT_FOUND"

    usn, hold_type = row
    if hold_type != "E":
        return None, "NOT_BANNED"

    cursor.execute(
        "UPDATE CF_USER SET HOLD_TYPE = 'A' WHERE USN = ?", usn
    )
    conn.commit()

    return {"usn": usn, "nick": ign}, "UNBANNED"


# =========================
# CHECK HOLD / BAN STATUS
# =========================
def check_hold_logic(ign: str):
    cursor = cursors.get("CF_SA_GAME")
    if not cursor:
        return None, "DB_ERROR"

    cursor.execute(
        "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK = ?", ign
    )
    row = cursor.fetchone()
    if not row:
        return None, "NOT_FOUND"

    usn, hold_type = row
    status = {"E": "BANNED", "A": "ACTIVE", "H": "HOLD"}.get(hold_type, "UNKNOWN")
    return {
        "usn": usn,
        "nick": ign,
        "hold_type": hold_type,
        "status": status,
    }, "OK"