# commands/gp/addgp.py

from discord.ext import commands
from database.connection import cursors, connections

class AddGP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addgp")
    async def addgp(self, ctx, ign: str = None, amount: int = None):
        if not ign or amount is None:
            await ctx.send("❌ Usage: !addgp <IGN> <amount>")
            return

        cursor = cursors.get("CF_SA_GAME")
        conn = connections.get("CF_SA_GAME")

        cursor.execute(
            "SELECT USN, GAME_POINT FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()

        if not row:
            await ctx.send("❌ Player not found")
            return

        usn, old_gp = row
        old_gp = old_gp or 0
        new_gp = old_gp + amount

        cursor.execute(
            "UPDATE CF_USER SET GAME_POINT=? WHERE USN=?",
            new_gp, usn
        )
        conn.commit()

        await ctx.send(
            f"✅ GP Updated\n"
            f"Player: `{ign}`\n"
            f"Old GP: `{old_gp:,}`\n"
            f"Added: `+{amount:,}`\n"
            f"New GP: `{new_gp:,}`"
        )

async def setup(bot):
    await bot.add_cog(AddGP(bot))