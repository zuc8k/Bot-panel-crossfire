# commands/game/ban.py

from discord.ext import commands
from datetime import datetime, timedelta
from database.connection import cursors, connections
from systems.ban_store import add_temp_ban

class BanPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    async def ban(self, ctx, ign: str = None, duration: str = None, *, reason: str = None):
        if not ign or not duration or not reason:
            await ctx.send("❌ Usage: !ban <IGN> <1h/1d/7d/perma> <reason>")
            return

        cursor = cursors.get("CF_SA_GAME")
        conn = connections.get("CF_SA_GAME")

        cursor.execute(
            "SELECT USN, NICK, HOLD_TYPE FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor.fetchone()
        if not row:
            await ctx.send("❌ Player not found")
            return

        usn, nick, hold = row
        if hold == "E":
            await ctx.send("⚠️ Player already banned")
            return

        release_date = None
        if duration.lower() != "perma":
            value = int(duration[:-1])
            unit = duration[-1]
            seconds = value * 3600 if unit == "h" else value * 86400
            release_date = datetime.now() + timedelta(seconds=seconds)

        cursor.execute(
            "UPDATE CF_USER SET HOLD_TYPE='E' WHERE USN=?",
            usn
        )
        conn.commit()

        if release_date:
            add_temp_ban(usn, ctx.author.name, reason, release_date, nick)

        await ctx.send(f"🔨 Banned {nick} | Duration: {duration}")

async def setup(bot):
    await bot.add_cog(BanPlayer(bot))