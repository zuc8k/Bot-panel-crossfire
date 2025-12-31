# commands/ranks/add.py

from discord.ext import commands
from core.ranks import (
    OWNER,
    ADMIN,
    GUARD,
    set_user_rank,
    get_user_rank
)

VALID_RANKS = {
    "OWNER": OWNER,
    "ADMIN": ADMIN,
    "GUARD": GUARD
}

class AddRank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    async def add(self, ctx, member, rank: str = None):
        # OWNER بس
        if get_user_rank(ctx.author.id) != OWNER:
            await ctx.send("❌ This command is for OWNER only")
            return

        if rank is None:
            await ctx.send("❌ Usage: !add @user <OWNER|ADMIN|GUARD>")
            return

        rank = rank.upper()
        if rank not in VALID_RANKS:
            await ctx.send("❌ Invalid rank (OWNER / ADMIN / GUARD)")
            return

        ok = set_user_rank(member.id, VALID_RANKS[rank])
        if not ok:
            await ctx.send("⚠️ You cannot change OWNER rank")
            return

        await ctx.send(
            f"✅ `{member}` is now `{rank}`"
        )

async def setup(bot):
    await bot.add_cog(AddRank(bot))