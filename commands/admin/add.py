# commands/admin/add.py

from discord.ext import commands
from core.ranks import set_user_rank, RANK_NAMES
from config.settings import OWNER_ID, ALLOWED_IDS

class AddUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    async def add(self, ctx, member: commands.MemberConverter = None, rank: str = "M"):
        if ctx.author.id != OWNER_ID:
            return

        if member is None:
            await ctx.send("❌ Usage: !add @user [M/G/A]")
            return

        rank = rank.upper()
        if rank not in ["M", "G", "A"]:
            await ctx.send("❌ Rank must be M, G, or A")
            return

        if member.id not in ALLOWED_IDS:
            ALLOWED_IDS.append(member.id)

        set_user_rank(member.id, rank)
        await ctx.send(f"✅ Added {member.mention} as {RANK_NAMES[rank]}")

async def setup(bot):
    await bot.add_cog(AddUser(bot))