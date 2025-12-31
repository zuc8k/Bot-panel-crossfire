# commands/ranks/add.py

from discord.ext import commands
from services.rank_service import add_rank
from core.ranks import OWNER

class AddRank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    async def add(self, ctx, member, rank: str = None):
        if rank is None:
            await ctx.send("❌ Usage: !add @user <OWNER|ADMIN|GUARD>")
            return

        # أمان: OWNER بس
        if ctx.author.id != ctx.guild.owner_id:
            await ctx.send("❌ Only OWNER can use this command")
            return

        rank = rank.upper()
        if rank not in ["OWNER", "ADMIN", "GUARD"]:
            await ctx.send("❌ Invalid rank")
            return

        add_rank(member.id, rank)
        await ctx.send(f"✅ `{member}` is now `{rank}`")

async def setup(bot):
    await bot.add_cog(AddRank(bot))