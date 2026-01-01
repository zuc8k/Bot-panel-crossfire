from database.connection import cursors
from datetime import datetime, timedelta

def get_daily_admin_report():
    cursor = cursors.get("CF_SA_GAME")

    yesterday = datetime.now() - timedelta(days=1)

    cursor.execute(
        """
        SELECT ADMIN_NAME, ACTION, COUNT(*) 
        FROM CF_ADMIN_LOG
        WHERE CREATED_AT >= ?
        GROUP BY ADMIN_NAME, ACTION
        """,
        yesterday
    )

    return cursor.fetchall()