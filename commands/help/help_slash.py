# commands/help/help_slash.py

import discord
from discord import app_commands
from discord.ext import commands

from services.help_service import build_help_menu
from core.ranks import get_user_rank, RANK_NAMES


class HelpSlash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="Show available commands based on your rank"
    )
    async def help_slash(self, interaction: discord.Interaction):

        rank = get_user_rank(interaction.user.id)
        rank_name = RANK_NAMES.get(rank, rank)

        menu = build_help_menu(rank)

        embed = discord.Embed(
            title="📖 Help Menu",
            description=f"👤 Rank: **{rank_name}**",
            color=0x2F3136
        )

        for category, commands_list in menu.items():
            embed.add_field(
                name=category,
                value="\n".join(f"/{cmd}" for cmd in commands_list),
                inline=False
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(HelpSlash(bot))