import discord
from discord import app_commands
from discord.ext import commands
from services.rank_service import set_player_rank

class SetRankSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="setrank",
        description="Change player in-game rank"
    )
    @app_commands.describe(
        ign="Player nickname",
        rank="A = Admin | G = Guardian | M = Member | N = Normal"
    )
    async def setrank(
        self,
        interaction: discord.Interaction,
        ign: str,
        rank: str
    ):
        result, status = set_player_rank(ign, rank)

        if status == "INVALID_RANK":
            return await interaction.response.send_message(
                "❌ Rank must be: A, G, M, N",
                ephemeral=True
            )

        if status == "NOT_FOUND":
            return await interaction.response.send_message(
                "❌ Player not found",
                ephemeral=True
            )

        if status == "SAME_RANK":
            return await interaction.response.send_message(
                "⚠️ Player already has this rank",
                ephemeral=True
            )

        await interaction.response.send_message(
            f"🎖️ Rank Updated\n"
            f"Player: `{ign}`\n"
            f"Rank: `{result['old_rank']}` ➜ `{result['new_rank']}`"
        )

async def setup(bot):
    await bot.add_cog(SetRankSlash(bot))