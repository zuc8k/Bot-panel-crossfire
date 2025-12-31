import discord
from discord import app_commands
from discord.ext import commands
import time

from database.connection import connections
from core.ranks import user_ranks

START_TIME = time.time()

class StatusSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="status",
        description="Show bot & database status"
    )
    async def status(self, interaction: discord.Interaction):

        uptime = int(time.time() - START_TIME)
        hours = uptime // 3600
        minutes = (uptime % 3600) // 60

        db_status = []
        for name, conn in connections.items():
            if conn:
                db_status.append(f"🟢 {name}")
            else:
                db_status.append(f"🔴 {name}")

        admin_count = list(user_ranks.values()).count("A")

        embed = discord.Embed(
            title="📊 System Status",
            color=0x57F287
        )

        embed.add_field(
            name="🤖 Bot",
            value="Online",
            inline=True
        )

        embed.add_field(
            name="⏱️ Uptime",
            value=f"{hours}h {minutes}m",
            inline=True
        )

        embed.add_field(
            name="🗄️ Databases",
            value="\n".join(db_status),
            inline=False
        )

        embed.add_field(
            name="👑 Admins",
            value=str(admin_count),
            inline=True
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(StatusSlash(bot))