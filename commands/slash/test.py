# commands/slash/test.py

import discord
from discord import app_commands
from discord.ext import commands

class SlashTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="Test slash command")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ Slash Command Working")

async def setup(bot):
    await bot.add_cog(SlashTest(bot))