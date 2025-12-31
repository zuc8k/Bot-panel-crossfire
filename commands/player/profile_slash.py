import discord
from discord import app_commands
from discord.ext import commands

from database.connection import cursors

class ProfileSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="profile",
        description="Show player profile"
    )
    @app_commands.describe(
        ign="Player nickname"
    )
    async def profile(
        self,
        interaction: discord.Interaction,
        ign: str
    ):
        cursor = cursors.get("CF_SA_GAME")

        if not cursor:
            return await interaction.response.send_message(
                "❌ Database not available",
                ephemeral=True
            )

        cursor.execute(
            """
            SELECT
                NICK,
                AUTHORITY,
                LEV,
                GAME_POINT,
                HOLD_TYPE
            FROM CF_USER
            WHERE NICK = ?
            """,
            ign
        )

        row = cursor.fetchone()

        if not row:
            return await interaction.response.send_message(
                "❌ Player not found",
                ephemeral=True
            )

        nick, rank, level, gp, hold = row

        rank_map = {
            "A": "👑 Admin",
            "G": "🛡️ Guardian",
            "M": "👤 Member",
            "N": "🎮 Normal"
        }

        embed = discord.Embed(
            title="🎮 Player Profile",
            color=0x3498DB
        )

        embed.add_field(name="Nick", value=nick, inline=True)
        embed.add_field(name="Rank", value=rank_map.get(rank, rank), inline=True)
        embed.add_field(name="Level", value=str(level), inline=True)
        embed.add_field(name="GP", value=str(gp), inline=True)
        embed.add_field(
            name="Status",
            value="🚫 Banned" if hold == "E" else "✅ Active",
            inline=True
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(ProfileSlash(bot))