# commands/account/genpass.py

from discord.ext import commands
from services.account_service import generate_password_logic

class GenPass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="genpass")
    async def genpass(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !genpass <IGN>")
            return

        new_pass = generate_password_logic(ign)
        if not new_pass:
            await ctx.send("❌ Account not found")
            return

        await ctx.send(
            f"🔐 New password for `{ign}`:\n"
            f"`{new_pass}`"
        )

async def setup(bot):
    await bot.add_cog(GenPass(bot))