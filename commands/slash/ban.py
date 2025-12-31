# commands/slash/ban.py

import discord
from discord import app_commands
from discord.ext import commands
from database.connection import cursors, connections

class SlashBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a player")
    @app_commands.describe(
        ign="Player name",
        reason="Reason for ban"
    )
    async def ban(self, interaction: discord.Interaction, ign: str, reason: str):
        cursor = cursors.get("CF_SA_GAME")
        conn = connections.get("CF_SA_GAME")

        cursor.execute(
            "SELECT USN, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()

        if not row:
            await interaction.response.send_message("❌ Player not found", ephemeral=True)
            return

        usn, hold = row
        if hold == "E":
            await interaction.response.send_message("⚠️ Player already banned", ephemeral=True)
            return

        cursor.execute(
            "UPDATE CF_USER SET HOLD_TYPE='E' WHERE USN=?",
            usn
        )
        conn.commit()

        await interaction.response.send_message(
            f"🔨 Player Banned\n"
            f"Nick: `{ign}`\n"
            f"Reason: {reason}"
        )

async def setup(bot):
    await bot.add_cog(SlashBan(bot))