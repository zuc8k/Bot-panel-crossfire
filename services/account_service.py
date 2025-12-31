# services/account_service.py

from database.connection import cursors, connections
from systems.account_utils import generate_password, hash_password_md5

def change_password_logic(ign: str, new_pass: str):
    cursor = cursors.get("CF_WEB")
    conn = connections.get("CF_WEB")

    hashed = hash_password_md5(new_pass)
    cursor.execute(
        "UPDATE CF_USER SET PASSWORD=? WHERE NICK=?",
        hashed, ign
    )

    if cursor.rowcount == 0:
        return False

    conn.commit()
    return True

def generate_password_logic(ign: str):
    cursor = cursors.get("CF_WEB")
    conn = connections.get("CF_WEB")

    new_pass = generate_password()
    hashed = hash_password_md5(new_pass)

    cursor.execute(
        "UPDATE CF_USER SET PASSWORD=? WHERE NICK=?",
        hashed, ign
    )

    if cursor.rowcount == 0:
        return None

    conn.commit()
    return new_pass

def change_name_logic(old_ign: str, new_ign: str):
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    cursor.execute(
        "UPDATE CF_USER SET NICK=? WHERE NICK=?",
        new_ign, old_ign
    )

    if cursor.rowcount == 0:
        return False

    conn.commit()
    return True

def check_account_logic(ign: str):
    cursor = cursors.get("CF_SA_GAME")
    cursor.execute(
        "SELECT USN, NICK, LEVEL, GP, HOLD_TYPE FROM CF_USER WHERE NICK=?",
        ign
    )
    row = cursor.fetchone()
    if not row:
        return None

    usn, nick, level, gp, hold = row
    status = "BANNED" if hold == "E" else "ACTIVE"

    return {
        "usn": usn,
        "nick": nick,
        "level": level,
        "gp": gp,
        "status": status
    }