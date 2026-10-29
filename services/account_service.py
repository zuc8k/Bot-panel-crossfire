# services/account_service.py
from database.connection import cursors, connections
from systems.account_utils import generate_password, hash_password_md5


def change_password_logic(ign: str, new_pass: str):
    cursor = cursors.get("CF_WEB")
    conn = connections.get("CF_WEB")
    if not cursor or not conn:
        return False

    try:
        hashed = hash_password_md5(new_pass)
        cursor.execute(
            "UPDATE CF_USER SET PASSWORD=? WHERE NICK=?", hashed, ign
        )
        if cursor.rowcount == 0:
            return False
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ change_password_logic error: {e}")
        try:
            conn.rollback()
        except Exception:
            pass
        return False


def generate_password_logic(ign: str):
    cursor = cursors.get("CF_WEB")
    conn = connections.get("CF_WEB")
    if not cursor or not conn:
        return None

    try:
        new_pass = generate_password()
        hashed = hash_password_md5(new_pass)
        cursor.execute(
            "UPDATE CF_USER SET PASSWORD=? WHERE NICK=?", hashed, ign
        )
        if cursor.rowcount == 0:
            return None
        conn.commit()
        return new_pass
    except Exception as e:
        print(f"❌ generate_password_logic error: {e}")
        try:
            conn.rollback()
        except Exception:
            pass
        return None


def change_name_logic(old_ign: str, new_ign: str):
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")
    if not cursor or not conn:
        return False

    try:
        cursor.execute(
            "UPDATE CF_USER SET NICK=? WHERE NICK=?", new_ign, old_ign
        )
        if cursor.rowcount == 0:
            return False
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ change_name_logic error: {e}")
        try:
            conn.rollback()
        except Exception:
            pass
        return False


def check_account_logic(ign: str):
    cursor = cursors.get("CF_SA_GAME")
    if not cursor:
        return None

    try:
        cursor.execute(
            "SELECT USN, NICK, LEVEL, GP, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign,
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
            "status": status,
        }
    except Exception as e:
        print(f"❌ check_account_logic error: {e}")
        return None