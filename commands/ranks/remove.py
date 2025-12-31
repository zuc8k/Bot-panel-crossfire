# commands/ranks/remove.py

from discord.ext import commands
from core.ranks import OWNER, remove_user_rank, get_user_rank

class RemoveRank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remove")
    async def remove(self, ctx, member):
        # OWNER بس
        if get_user_rank(ctx.author.id) != OWNER:
            await ctx.send("❌ This command is for OWNER only")
            return

        if get_user_rank(member.id) == OWNER:
            await ctx.send("⚠️ You cannot remove OWNER rank")
            return

        remove_user_rank(member.id)

        await ctx.send(
            f"🗑️ Rank removed from `{member}`"
        )

async def setup(bot):
    await bot.add_cog(RemoveRank(bot))