# commands/ban/ban.py

from discord.ext import commands
from services.ban_service import ban_player_logic

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    async def ban(self, ctx, ign: str = None, duration: str = None, *, reason: str = None):
        if not ign or not duration or not reason:
            await ctx.send("❌ Usage: !ban <IGN> <duration> <reason>")
            return

        data, status = ban_player_logic(ign, duration)

        if status == "DB_ERROR":
            await ctx.send("❌ Database connection error")
            return

        if status == "NOT_FOUND":
            await ctx.send("❌ Player not found")
            return

        if status == "ALREADY_BANNED":
            await ctx.send("⚠️ Player already banned")
            return

        await ctx.send(
            f"🔨 Player Banned\n"
            f"Nick: `{data['nick']}`\n"
            f"Duration: `{duration}`\n"
            f"Reason: {reason}"
        )

async def setup(bot):
    await bot.add_cog(Ban(bot))