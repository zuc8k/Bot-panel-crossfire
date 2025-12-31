# commands/gp/gplogs.py

from discord.ext import commands
from database.connection import cursors

class GPLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gplogs")
    async def gplogs(self, ctx, ign: str = None):
        cursor = cursors.get("CF_WEB")

        if ign:
            cursor.execute(
                "SELECT TOP 10 ign, gp_added, admin, date FROM gp_logs WHERE ign=? ORDER BY date DESC",
                ign
            )
        else:
            cursor.execute(
                "SELECT TOP 10 ign, gp_added, admin, date FROM gp_logs ORDER BY date DESC"
            )

        rows = cursor.fetchall()
        if not rows:
            await ctx.send("📭 No GP logs found")
            return

        msg = "📋 GP Logs\n"
        for ign, added, admin, date in rows:
            msg += f"- {ign} | +{added} | {admin} | {date}\n"

        await ctx.send(f"```{msg}```")

async def setup(bot):
    await bot.add_cog(GPLogs(bot))