# commands/slash/addzp.py

import discord
from discord import app_commands
from discord.ext import commands
from services.zp_service import add_zp_logic
from systems.zp_utils import format_zp

class SlashAddZP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="addzp", description="Add ZP to player")
    async def addzp(self, interaction: discord.Interaction, ign: str, amount: int):
        data = add_zp_logic(ign, amount)
        if not data:
            await interaction.response.send_message(
                "❌ Player not found",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"💎 ZP Added\n"
            f"Player: `{data['nick']}`\n"
            f"Old ZP: {format_zp(data['old_zp'])}\n"
            f"Added: {format_zp(data['added'])}\n"
            f"New ZP: {format_zp(data['new_zp'])}"
        )

async def setup(bot):
    await bot.add_cog(SlashAddZP(bot))