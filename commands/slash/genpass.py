# commands/slash/genpass.py

import discord
from discord import app_commands
from discord.ext import commands
from services.account_service import generate_password_logic

class SlashGenPass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="genpass", description="Generate new password")
    async def genpass(self, interaction: discord.Interaction, ign: str):
        new_pass = generate_password_logic(ign)
        if not new_pass:
            await interaction.response.send_message("❌ Account not found", ephemeral=True)
            return

        await interaction.response.send_message(
            f"🔐 New password for `{ign}`:\n"
            f"`{new_pass}`",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(SlashGenPass(bot))