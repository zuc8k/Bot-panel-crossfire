# database/logs.py

from database.connection import cursors, connections
from systems.log_utils import generate_log_id

def log_action(action: str, ign: str, old_value, new_value, admin: str):
    cursor = cursors.get("CF_WEB")
    conn = connections.get("CF_WEB")

    if not cursor or not conn:
        return False

    log_id = generate_log_id()

    try:
        cursor.execute("""
            INSERT INTO logs (id, action, ign, old_value, new_value, [by])
            VALUES (?, ?, ?, ?, ?, ?)
        """, log_id, action, ign, str(old_value), str(new_value), admin)

        conn.commit()
        return True
    except Exception:
        try:
            conn.rollback()
        except:
            pass
        return False