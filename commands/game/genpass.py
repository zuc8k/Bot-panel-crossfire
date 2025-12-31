# commands/game/genpass.py

from discord.ext import commands
from database.connection import cursors, connections
from systems.account_utils import generate_password, hash_password_md5

class GeneratePassword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="genpass")
    async def genpass(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !genpass <IGN>")
            return

        cursor = cursors.get("CF_WEB")
        conn = connections.get("CF_WEB")

        new_pass = generate_password()
        hashed = hash_password_md5(new_pass)

        cursor.execute(
            "UPDATE CF_USER SET PASSWORD=? WHERE NICK=?",
            hashed, ign
        )
        if cursor.rowcount == 0:
            await ctx.send("❌ Account not found")
            return

        conn.commit()
        await ctx.send(
            f"🔐 New password generated for `{ign}`:\n"
            f"`{new_pass}`"
        )

async def setup(bot):
    await bot.add_cog(GeneratePassword(bot))