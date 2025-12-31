# commands/ban/ban.py

from discord.ext import commands
from datetime import datetime
from database.connection import cursors, connections
from systems.ban_utils import parse_duration

class BanPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    async def ban(self, ctx, ign: str = None, duration: str = None, *, reason: str = None):
        if not ign or not duration or not reason:
            await ctx.send("❌ Usage: !ban <IGN> <duration> <reason>")
            return

        cursor = cursors.get("CF_SA_GAME")
        conn = connections.get("CF_SA_GAME")

        cursor.execute(
            "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()

        if not row:
            await ctx.send("❌ Player not found")
            return

        usn, hold = row
        if hold == "E":
            await ctx.send("⚠️ Player already banned")
            return

        release_date = parse_duration(duration)

        cursor.execute(
            "UPDATE CF_USER SET HOLD_TYPE='E' WHERE USN=?",
            usn
        )
        conn.commit()

        await ctx.send(
            f"🔨 Player Banned\n"
            f"Nick: `{ign}`\n"
            f"Duration: `{duration}`\n"
            f"Reason: {reason}"
        )

async def setup(bot):
    await bot.add_cog(BanPlayer(bot))