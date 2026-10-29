# commands/ban/ban_slash.py
import discord
from discord import app_commands
from discord.ext import commands
from services.ban_service import ban_player_logic
from services.admin_log_service import send_admin_log


class BanSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a player")
    @app_commands.describe(
        ign="Player name",
        duration="Duration like 1h / 1d / perma",
        reason="Reason for ban",
    )
    async def ban_slash(
        self,
        interaction: discord.Interaction,
        ign: str,
        duration: str,
        reason: str,
    ):
        data, status = ban_player_logic(ign, duration)
        if status != "BANNED":
            await interaction.response.send_message(
                f"❌ Error: {status}", ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"🔨 Player `{ign}` banned for `{duration}`\n Reason: {reason}",
            ephemeral=True,
        )

        # تسجيل الإجراء في سجل الإدارة
        try:
            await send_admin_log(
                self.bot,
                action="BAN",
                admin=interaction.user,
                target=ign,
                details=f"Duration: {duration} | Reason: {reason}",
            )
        except Exception as e:
            print(f"⚠️ Failed to log ban action: {e}")


async def setup(bot):
    await bot.add_cog(BanSlash(bot))