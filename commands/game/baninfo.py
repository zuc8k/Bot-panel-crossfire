# commands/game/baninfo.py

from discord.ext import commands
from database.connection import cursors
from systems.ban_store import get_ban
from datetime import datetime

class BanInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="baninfo")
    async def baninfo(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !baninfo <IGN>")
            return

        cursor = cursors.get("CF_SA_GAME")
        cursor.execute(
            "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()
        if not row:
            await ctx.send("❌ Player not found")
            return

        usn, hold = row
        if hold != "E":
            await ctx.send("🟢 Player is not banned")
            return

        data = get_ban(usn)
        if not data:
            await ctx.send("🔴 Permanent ban")
            return

        remaining = data["release_date"] - datetime.now()
        await ctx.send(
            f"🔴 Banned\n"
            f"Admin: {data['admin']}\n"
            f"Reason: {data['reason']}\n"
            f"Remaining: {remaining}"
        )

async def setup(bot):
    await bot.add_cog(BanInfo(bot))