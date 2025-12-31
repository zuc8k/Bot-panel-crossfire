# commands/account/changename.py

from discord.ext import commands
from services.account_service import change_name_logic

class ChangeName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changename")
    async def changename(self, ctx, old_ign: str = None, new_ign: str = None):
        if not old_ign or not new_ign:
            await ctx.send("❌ Usage: !changename <old_ign> <new_ign>")
            return

        ok = change_name_logic(old_ign, new_ign)
        if not ok:
            await ctx.send("❌ Player not found")
            return

        await ctx.send(f"✏️ Name changed: `{old_ign}` → `{new_ign}`")

async def setup(bot):
    await bot.add_cog(ChangeName(bot))