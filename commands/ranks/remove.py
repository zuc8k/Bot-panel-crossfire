# commands/ranks/remove.py

from discord.ext import commands
from services.rank_service import remove_rank

class RemoveRank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remove")
    async def remove(self, ctx, member):
        # OWNER بس
        if ctx.author.id != ctx.guild.owner_id:
            await ctx.send("❌ Only OWNER can use this command")
            return

        ok = remove_rank(member.id)
        if not ok:
            await ctx.send("❌ User has no rank")
            return

        await ctx.send(f"🗑️ Rank removed from `{member}`")

async def setup(bot):
    await bot.add_cog(RemoveRank(bot))