from discord.ext import commands
from services.rank_service import set_player_rank

class SetRankPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setrank")
    async def setrank(self, ctx, ign: str, rank: str):

        result, status = set_player_rank(ign, rank)

        if status == "INVALID_RANK":
            return await ctx.send("❌ Rank must be: A, G, M, N")

        if status == "NOT_FOUND":
            return await ctx.send("❌ Player not found")

        if status == "SAME_RANK":
            return await ctx.send("⚠️ Player already has this rank")

        await ctx.send(
            f"🎖️ Rank Updated\n"
            f"Player: `{ign}`\n"
            f"Rank: `{result['old_rank']}` ➜ `{result['new_rank']}`"
        )

async def setup(bot):
    await bot.add_cog(SetRankPrefix(bot))