# commands/ban/banlist.py

from discord.ext import commands
from database.connection import cursors

class BanList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="banlist")
    async def banlist(self, ctx):
        cursor = cursors.get("CF_SA_GAME")
        cursor.execute(
            "SELECT NICK, USN FROM CF_USER WHERE HOLD_TYPE='E'"
        )
        rows = cursor.fetchall()

        if not rows:
            await ctx.send("🎉 No banned players")
            return

        msg = "🚫 Ban List\n"
        for nick, usn in rows:
            msg += f"- {nick} | USN: {usn}\n"

        await ctx.send(f"```{msg}```")

async def setup(bot):
    await bot.add_cog(BanList(bot))