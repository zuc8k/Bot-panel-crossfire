# commands/help/help_slash.py

import discord
from discord import app_commands
from discord.ext import commands

from core.ranks import get_user_rank, RANK_NAMES
from ui.help_view import HelpView

class HelpSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="Show interactive help menu"
    )
    async def help(self, interaction: discord.Interaction):

        rank = get_user_rank(interaction.user.id)
        rank_name = RANK_NAMES.get(rank, rank)

        embed = discord.Embed(
            title="📖 Help Menu",
            description=f"👤 Rank: **{rank_name}**\nاختر قسم من القائمة 👇",
            color=0x2F3136
        )

        view = HelpView(rank)

        await interaction.response.send_message(
            embed=embed,
            view=view,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(HelpSlash(bot))