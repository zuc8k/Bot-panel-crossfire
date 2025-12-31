# commands/admin/remove.py

from discord.ext import commands
from config.settings import OWNER_ID, ALLOWED_IDS
from core.ranks import remove_user_rank

class RemoveUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remove")
    async def remove(self, ctx, member: commands.MemberConverter = None):
        if ctx.author.id != OWNER_ID:
            return

        if member is None:
            await ctx.send("❌ Usage: !remove @user")
            return

        if member.id == OWNER_ID:
            await ctx.send("❌ Cannot remove owner")
            return

        if member.id in ALLOWED_IDS:
            ALLOWED_IDS.remove(member.id)

        remove_user_rank(member.id)
        await ctx.send(f"❌ Removed {member.mention}")

async def setup(bot):
    await bot.add_cog(RemoveUser(bot))