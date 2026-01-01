from database.connection import cursors, connections
from core.ranks import remove_user_rank

MAX_STRIKES = 3

def add_strike(admin):
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    cursor.execute(
        "INSERT INTO CF_ADMIN_STRIKES (ADMIN_ID, ADMIN_NAME, REASON) VALUES (?, ?, ?)",
        admin.id,
        str(admin),
        "Abuse / Misuse"
    )
    conn.commit()

    cursor.execute(
        "SELECT COUNT(*) FROM CF_ADMIN_STRIKES WHERE ADMIN_ID = ?",
        admin.id
    )
    strikes = cursor.fetchone()[0]

    if strikes >= MAX_STRIKES:
        remove_user_rank(admin.id)
        return True, strikes  # removed

    return False, strikes