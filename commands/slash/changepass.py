# commands/slash/changepass.py

import discord
from discord import app_commands
from discord.ext import commands
from services.account_service import change_password_logic

class SlashChangePass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="changepass", description="Change account password")
    async def changepass(self, interaction: discord.Interaction, ign: str, new_pass: str):
        ok = change_password_logic(ign, new_pass)
        if not ok:
            await interaction.response.send_message("❌ Account not found", ephemeral=True)
            return

        await interaction.response.send_message(f"🔐 Password changed for `{ign}`")

async def setup(bot):
    await bot.add_cog(SlashChangePass(bot))