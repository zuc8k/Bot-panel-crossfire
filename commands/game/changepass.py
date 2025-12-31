# commands/game/changepass.py

from discord.ext import commands
from database.connection import cursors, connections
from systems.account_utils import hash_password_md5

class ChangePassword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changepass")
    async def changepass(self, ctx, ign: str = None, new_pass: str = None):
        if not ign or not new_pass:
            await ctx.send("❌ Usage: !changepass <IGN> <new_password>")
            return

        cursor = cursors.get("CF_WEB")
        conn = connections.get("CF_WEB")

        hashed = hash_password_md5(new_pass)

        cursor.execute(
            "UPDATE CF_USER SET PASSWORD=? WHERE NICK=?",
            hashed, ign
        )
        if cursor.rowcount == 0:
            await ctx.send("❌ Account not found")
            return

        conn.commit()
        await ctx.send(f"🔐 Password changed for `{ign}`")

async def setup(bot):
    await bot.add_cog(ChangePassword(bot))