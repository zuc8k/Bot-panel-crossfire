# commands/account/changepass.py

from discord.ext import commands
from services.account_service import change_password_logic

class ChangePass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changepass")
    async def changepass(self, ctx, ign: str = None, new_pass: str = None):
        if not ign or not new_pass:
            await ctx.send("❌ Usage: !changepass <IGN> <new_pass>")
            return

        ok = change_password_logic(ign, new_pass)
        if not ok:
            await ctx.send("❌ Account not found")
            return

        await ctx.send(f"🔐 Password changed for `{ign}`")

async def setup(bot):
    await bot.add_cog(ChangePass(bot))