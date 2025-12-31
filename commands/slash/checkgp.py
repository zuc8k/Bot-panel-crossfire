# commands/slash/checkgp.py

import discord
from discord import app_commands
from discord.ext import commands
from database.connection import cursors
from systems.gp_utils import gp_rank

class SlashCheckGP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="checkgp", description="Check player GP")
    @app_commands.describe(ign="Player name")
    async def checkgp(self, interaction: discord.Interaction, ign: str):
        cursor = cursors.get("CF_SA_GAME")
        cursor.execute(
            "SELECT USN, NICK, GAME_POINT FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()

        if not row:
            await interaction.response.send_message("❌ Player not found", ephemeral=True)
            return

        usn, nick, gp = row
        gp = gp or 0

        await interaction.response.send_message(
            f"💰 GP Info\n"
            f"Nick: `{nick}`\n"
            f"USN: `{usn}`\n"
            f"GP: `{gp:,}`\n"
            f"Rank: {gp_rank(gp)}"
        )

async def setup(bot):
    await bot.add_cog(SlashCheckGP(bot))