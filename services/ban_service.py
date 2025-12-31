# services/ban_service.py

from datetime import datetime
from database.connection import cursors, connections
from systems.ban_utils import parse_duration


def ban_player_logic(ign: str, duration: str):
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    if not cursor or not conn:
        return None, "DB_ERROR"

    cursor.execute(
        "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK = ?",
        ign
    )
    row = cursor.fetchone()

    if not row:
        return None, "NOT_FOUND"

    usn, hold_type = row

    if hold_type == "E":
        return None, "ALREADY_BANNED"

    release_date = parse_duration(duration)

    cursor.execute(
        "UPDATE CF_USER SET HOLD_TYPE = 'E' WHERE USN = ?",
        usn
    )
    conn.commit()

    return {
        "usn": usn,
        "nick": ign,
        "release_date": release_date
    }, "BANNED"