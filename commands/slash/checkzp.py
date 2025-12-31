# commands/slash/checkzp.py

import discord
from discord import app_commands
from discord.ext import commands
from services.zp_service import check_zp_logic
from systems.zp_utils import format_zp

class SlashCheckZP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="checkzp", description="Check player ZP")
    async def checkzp(self, interaction: discord.Interaction, ign: str):
        data = check_zp_logic(ign)
        if not data:
            await interaction.response.send_message(
                "❌ Player not found",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"💎 ZP Balance\n"
            f"Player: `{data['nick']}`\n"
            f"ZP: {format_zp(data['zp'])}"
        )

async def setup(bot):
    await bot.add_cog(SlashCheckZP(bot))