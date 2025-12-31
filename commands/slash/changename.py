# commands/slash/changename.py

import discord
from discord import app_commands
from discord.ext import commands
from services.account_service import change_name_logic

class SlashChangeName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="changename", description="Change player name")
    async def changename(self, interaction: discord.Interaction, old_ign: str, new_ign: str):
        ok = change_name_logic(old_ign, new_ign)
        if not ok:
            await interaction.response.send_message("❌ Player not found", ephemeral=True)
            return

        await interaction.response.send_message(
            f"✏️ Name changed: `{old_ign}` → `{new_ign}`"
        )

async def setup(bot):
    await bot.add_cog(SlashChangeName(bot))