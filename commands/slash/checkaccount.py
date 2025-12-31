# commands/slash/checkaccount.py

import discord
from discord import app_commands
from discord.ext import commands
from services.account_service import check_account_logic

class SlashCheckAccount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="checkaccount", description="Check account info")
    async def checkaccount(self, interaction: discord.Interaction, ign: str):
        data = check_account_logic(ign)
        if not data:
            await interaction.response.send_message("❌ Account not found", ephemeral=True)
            return

        await interaction.response.send_message(
            f"👤 Account Info\n"
            f"Nick: `{data['nick']}`\n"
            f"USN: `{data['usn']}`\n"
            f"Level: `{data['level']}`\n"
            f"GP: `{data['gp']}`\n"
            f"Status: `{data['status']}`"
        )

async def setup(bot):
    await bot.add_cog(SlashCheckAccount(bot))