# services/rank_service.py

from database.connection import cursors, connections

# رتب اللعبة فقط
VALID_GAME_RANKS = ["A", "G", "M", "N"]

def set_game_rank(ign: str, new_rank: str):
    new_rank = new_rank.upper()

    if new_rank not in VALID_GAME_RANKS:
        return None, "INVALID_RANK"

    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    if not cursor or not conn:
        return None, "DB_ERROR"

    cursor.execute(
        "SELECT USN, AUTHORITY FROM CF_USER WHERE NICK = ?",
        ign
    )
    row = cursor.fetchone()

    if not row:
        return None, "NOT_FOUND"

    usn, old_rank = row

    if old_rank == new_rank:
        return None, "SAME_RANK"

    cursor.execute(
        """
        UPDATE CF_USER
        SET AUTHORITY = ?
        WHERE USN = ?
        """,
        new_rank, usn
    )
    conn.commit()

    return {
        "usn": usn,
        "nick": ign,
        "old_rank": old_rank,
        "new_rank": new_rank
    }, "UPDATED"