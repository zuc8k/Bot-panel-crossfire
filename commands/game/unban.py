# commands/game/unban.py

from discord.ext import commands
from database.connection import cursors, connections
from systems.ban_store import remove_ban

class UnbanPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unban")
    async def unban(self, ctx, ign: str = None, *, reason: str = None):
        if not ign or not reason:
            await ctx.send("❌ Usage: !unban <IGN> <reason>")
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
        if hold != "E":
            await ctx.send("ℹ️ Player is not banned")
            return

        cursor.execute(
            "UPDATE CF_USER SET HOLD_TYPE='A' WHERE USN=?",
            usn
        )
        conn.commit()
        remove_ban(usn)

        await ctx.send(f"🔓 Unbanned {ign}")

async def setup(bot):
    await bot.add_cog(UnbanPlayer(bot))