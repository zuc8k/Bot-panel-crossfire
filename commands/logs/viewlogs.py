# commands/logs/viewlogs.py

from discord.ext import commands
from database.connection import cursors

class ViewLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="logs")
    async def logs(self, ctx, ign: str = None, limit: int = 10):
        limit = min(limit, 20)
        cursor = cursors.get("CF_WEB")

        if ign:
            cursor.execute("""
                SELECT TOP (?) action, ign, old_value, new_value, [by], date
                FROM logs
                WHERE ign=?
                ORDER BY date DESC
            """, limit, ign)
        else:
            cursor.execute("""
                SELECT TOP (?) action, ign, old_value, new_value, [by], date
                FROM logs
                ORDER BY date DESC
            """, limit)

        rows = cursor.fetchall()

        if not rows:
            await ctx.send("📭 No logs found")
            return

        msg = "📋 System Logs\n"
        for action, ign, old_v, new_v, admin, date in rows:
            msg += (
                f"- [{date}] {action}\n"
                f"  Player: {ign}\n"
                f"  {old_v} → {new_v}\n"
                f"  By: {admin}\n\n"
            )

        await ctx.send(f"```{msg}```")

async def setup(bot):
    await bot.add_cog(ViewLogs(bot))