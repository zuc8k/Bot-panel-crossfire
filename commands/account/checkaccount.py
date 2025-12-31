# commands/account/checkaccount.py

from discord.ext import commands
from services.account_service import check_account_logic

class CheckAccount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="checkaccount")
    async def checkaccount(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !checkaccount <IGN>")
            return

        data = check_account_logic(ign)
        if not data:
            await ctx.send("❌ Account not found")
            return

        await ctx.send(
            f"👤 Account Info\n"
            f"Nick: `{data['nick']}`\n"
            f"USN: `{data['usn']}`\n"
            f"Level: `{data['level']}`\n"
            f"GP: `{data['gp']}`\n"
            f"Status: `{data['status']}`"
        )

async def setup(bot):
    await bot.add_cog(CheckAccount(bot))