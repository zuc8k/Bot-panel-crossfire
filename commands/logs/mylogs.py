# commands/logs/mylogs.py

from discord.ext import commands
from database.connection import cursors

class MyLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mylogs")
    async def mylogs(self, ctx, limit: int = 10):
        limit = min(limit, 20)
        cursor = cursors.get("CF_WEB")

        cursor.execute("""
            SELECT TOP (?) action, ign, old_value, new_value, date
            FROM logs
            WHERE [by]=?
            ORDER BY date DESC
        """, limit, ctx.author.name)

        rows = cursor.fetchall()

        if not rows:
            await ctx.send("📭 You have no logs")
            return

        msg = f"📋 Logs by {ctx.author.name}\n"
        for action, ign, old_v, new_v, date in rows:
            msg += (
                f"- [{date}] {action}\n"
                f"  Player: {ign}\n"
                f"  {old_v} → {new_v}\n\n"
            )

        await ctx.send(f"```{msg}```")

async def setup(bot):
    await bot.add_cog(MyLogs(bot))