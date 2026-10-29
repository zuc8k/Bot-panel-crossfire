# tasks/auto_unban.py
from discord.ext import tasks
from datetime import datetime
from database.connection import cursors, connections
from systems.ban_store import all_bans, remove_ban


def start_auto_unban(bot):
    @tasks.loop(minutes=5)
    async def auto_unban():
        cursor = cursors.get("CF_SA_GAME")
        conn = connections.get("CF_SA_GAME")
        if not cursor or not conn:
            print("⚠️ auto_unban: database connection unavailable")
            return

        now = datetime.now()
        for usn, data in list(all_bans()):
            if data["release_date"] <= now:
                try:
                    cursor.execute(
                        "UPDATE CF_USER SET HOLD_TYPE='A' WHERE USN=?", usn
                    )
                    conn.commit()
                    remove_ban(usn)
                    print(f"✅ Auto-unbanned USN: {usn}")
                except Exception as e:
                    print(f"❌ auto_unban failed for USN {usn}: {e}")

    auto_unban.start()