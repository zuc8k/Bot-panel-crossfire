# commands/slash/unban.py

import discord
from discord import app_commands
from discord.ext import commands
from services.ban_service import unban_player_logic

class SlashUnban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unban", description="Unban a player")
    @app_commands.describe(
        ign="Player name",
        reason="Reason for unban"
    )
    async def unban(self, interaction: discord.Interaction, ign: str, reason: str):
        data, status = unban_player_logic(ign)

        if status == "NOT_FOUND":
            await interaction.response.send_message("❌ Player not found", ephemeral=True)
            return
        if status == "NOT_BANNED":
            await interaction.response.send_message("ℹ️ Player is not banned", ephemeral=True)
            return

        await interaction.response.send_message(
            f"🔓 Player Unbanned\n"
            f"Nick: `{data['nick']}`\n"
            f"Reason: {reason}"
        )

async def setup(bot):
    await bot.add_cog(SlashUnban(bot))