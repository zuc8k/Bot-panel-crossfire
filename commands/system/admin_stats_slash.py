import discord
from discord import app_commands
from discord.ext import commands
from services.admin_stats_service import get_admin_stats

class AdminStatsSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="admin-stats",
        description="Show admin performance statistics"
    )
    async def admin_stats(self, interaction: discord.Interaction):

        rows = get_admin_stats()

        if not rows:
            return await interaction.response.send_message(
                "❌ No stats available",
                ephemeral=True
            )

        stats = {}
        for admin, action, total in rows:
            stats.setdefault(admin, {})
            stats[admin][action] = total

        embed = discord.Embed(
            title="📊 Admin Performance",
            color=0x9B59B6
        )

        for admin, actions in stats.items():
            text = "\n".join(
                f"• {action}: {count}"
                for action, count in actions.items()
            )
            embed.add_field(
                name=admin,
                value=text,
                inline=False
            )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(AdminStatsSlash(bot))