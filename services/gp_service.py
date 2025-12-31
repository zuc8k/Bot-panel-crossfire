# services/gp_service.py

from database.connection import cursors
from systems.gp_utils import gp_rank

def check_gp_logic(ign: str):
    cursor = cursors.get("CF_SA_GAME")
    cursor.execute(
        "SELECT USN, NICK, GAME_POINT FROM CF_USER WHERE NICK=?",
        ign
    )
    row = cursor.fetchone()

    if not row:
        return None

    usn, nick, gp = row
    gp = gp or 0

    return {
        "usn": usn,
        "nick": nick,
        "gp": gp,
        "rank": gp_rank(gp)
    }