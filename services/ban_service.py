# services/ban_service.py

from database.connection import cursors, connections

def get_player(ign: str):
    cursor = cursors.get("CF_SA_GAME")
    cursor.execute(
        "SELECT USN, NICK, HOLD_TYPE FROM CF_USER WHERE NICK=? OR LOWER_NICK=?",
        ign, ign.lower()
    )
    return cursor.fetchone()

def ban_player_logic(ign: str):
    data = get_player(ign)
    if not data:
        return None, "NOT_FOUND"

    usn, nick, hold = data
    if hold == "E":
        return None, "ALREADY_BANNED"

    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    cursor.execute(
        "UPDATE CF_USER SET HOLD_TYPE='E' WHERE USN=?",
        usn
    )
    conn.commit()

    return {
        "usn": usn,
        "nick": nick
    }, "BANNED"

def unban_player_logic(ign: str):
    data = get_player(ign)
    if not data:
        return None, "NOT_FOUND"

    usn, nick, hold = data
    if hold != "E":
        return None, "NOT_BANNED"

    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    cursor.execute(
        "UPDATE CF_USER SET HOLD_TYPE='A' WHERE USN=?",
        usn
    )
    conn.commit()

    return {
        "usn": usn,
        "nick": nick
    }, "UNBANNED"