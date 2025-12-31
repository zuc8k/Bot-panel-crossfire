# commands/game/checkaccount.py

from discord.ext import commands
from database.connection import cursors

class CheckAccount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="checkaccount")
    async def checkaccount(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !checkaccount <IGN>")
            return

        cursor = cursors.get("CF_SA_GAME")
        cursor.execute(
            "SELECT USN, NICK, LEVEL, GP, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()
        if not row:
            await ctx.send("❌ Account not found")
            return

        usn, nick, level, gp, hold = row
        status = "🔴 BANNED" if hold == "E" else "🟢 ACTIVE"

        await ctx.send(
            f"👤 Account Info\n"
            f"USN: `{usn}`\n"
            f"Nick: `{nick}`\n"
            f"Level: `{level}`\n"
            f"GP: `{gp}`\n"
            f"Status: {status}"
        )

async def setup(bot):
    await bot.add_cog(CheckAccount(bot))