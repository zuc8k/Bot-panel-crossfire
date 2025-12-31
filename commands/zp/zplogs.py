# commands/zp/zplogs.py

from discord.ext import commands
from database.connection import cursors

class ZPLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="zplogs")
    async def zplogs(self, ctx, ign: str = None):
        cursor = cursors.get("CF_WEB")

        if ign:
            cursor.execute(
                "SELECT TOP 10 ign, count, leh, [from], date FROM addzp WHERE ign=? ORDER BY date DESC",
                ign
            )
        else:
            cursor.execute(
                "SELECT TOP 10 ign, count, leh, [from], date FROM addzp ORDER BY date DESC"
            )

        rows = cursor.fetchall()
        if not rows:
            await ctx.send("📭 No ZP logs found")
            return

        msg = "📋 ZP Logs\n"
        for ign, count, reason, admin, date in rows:
            msg += f"- {ign} | +{count} ZP | {admin} | {date}\n"

        await ctx.send(f"```{msg}```")

async def setup(bot):
    await bot.add_cog(ZPLogs(bot))