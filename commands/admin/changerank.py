# commands/admin/changerank.py

from discord.ext import commands
from core.ranks import set_user_rank, get_user_rank, RANK_NAMES
from config.settings import OWNER_ID

class ChangeRank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changerank")
    async def changerank(self, ctx, member: commands.MemberConverter = None, rank: str = None):
        if ctx.author.id != OWNER_ID:
            return

        if member is None or rank is None:
            await ctx.send("❌ Usage: !changerank @user [M/G/A]")
            return

        rank = rank.upper()
        if rank not in ["M", "G", "A"]:
            await ctx.send("❌ Rank must be M, G, or A")
            return

        old_rank = get_user_rank(member.id)
        set_user_rank(member.id, rank)

        await ctx.send(
            f"🔄 {member.mention} rank changed "
            f"from {RANK_NAMES[old_rank]} to {RANK_NAMES[rank]}"
        )

async def setup(bot):
    await bot.add_cog(ChangeRank(bot))