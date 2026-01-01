from database.connection import cursors

def get_player_live_status(ign: str):
    cursor = cursors.get("CF_SA_GAME")

    cursor.execute(
        """
        SELECT U.NICK, S.ROOM_ID, S.STATE
        FROM CF_USER U
        LEFT JOIN CF_USER_SESSION S ON U.USN = S.USN
        WHERE U.NICK = ?
        """,
        ign
    )

    row = cursor.fetchone()

    if not row:
        return None

    nick, room_id, state = row

    if not state:
        return {
            "status": "OFFLINE"
        }

    return {
        "status": state,
        "room_id": room_id
    }