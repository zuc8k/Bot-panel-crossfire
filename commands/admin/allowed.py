# commands/admin/allowed.py

from discord.ext import commands
from config.settings import ALLOWED_IDS
from core.ranks import get_user_rank, RANK_NAMES

class AllowedList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="allowed")
    async def allowed(self, ctx):
        lines = []
        for uid in ALLOWED_IDS:
            rank = get_user_rank(uid)
            lines.append(f"{uid} - {RANK_NAMES.get(rank, rank)}")

        await ctx.send("👥 Allowed Users:\n" + "\n".join(lines))

async def setup(bot):
    await bot.add_cog(AllowedList(bot))