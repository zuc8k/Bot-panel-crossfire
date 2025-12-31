# commands/gp/checkgp.py

from discord.ext import commands
from database.connection import cursors
from systems.gp_utils import gp_rank

class CheckGP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="checkgp")
    async def checkgp(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !checkgp <IGN>")
            return

        cursor = cursors.get("CF_SA_GAME")
        cursor.execute(
            "SELECT USN, NICK, GAME_POINT FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()

        if not row:
            await ctx.send("❌ Player not found")
            return

        usn, nick, gp = row
        gp = gp or 0

        await ctx.send(
            f"💰 GP Info\n"
            f"Nick: `{nick}`\n"
            f"USN: `{usn}`\n"
            f"GP: `{gp:,}`\n"
            f"Rank: {gp_rank(gp)}"
        )

async def setup(bot):
    await bot.add_cog(CheckGP(bot))