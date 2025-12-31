# commands/ban/checkhold.py

from discord.ext import commands
from database.connection import cursors

class CheckHold(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="checkhold")
    async def checkhold(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !checkhold <IGN>")
            return

        cursor = cursors.get("CF_SA_GAME")
        cursor.execute(
            "SELECT USN, NICK, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()

        if not row:
            await ctx.send("❌ Player not found")
            return

        usn, nick, hold = row
        status = "🔴 BANNED" if hold == "E" else "🟢 ACTIVE"

        await ctx.send(
            f"🔎 Hold Status\n"
            f"Nick: `{nick}`\n"
            f"USN: `{usn}`\n"
            f"Status: {status}"
        )

async def setup(bot):
    await bot.add_cog(CheckHold(bot))