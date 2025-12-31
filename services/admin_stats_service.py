from database.connection import cursors

def get_admin_stats(limit: int = 10):
    cursor = cursors.get("CF_SA_GAME")
    if not cursor:
        return None

    cursor.execute(
        """
        SELECT
            ADMIN_NAME,
            ACTION,
            COUNT(*) AS TOTAL
        FROM CF_ADMIN_LOG
        GROUP BY ADMIN_NAME, ACTION
        ORDER BY TOTAL DESC
        """
    )

    rows = cursor.fetchall()
    return rows