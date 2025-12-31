# commands/game/banlist.py

from discord.ext import commands
from systems.ban_store import all_bans
from datetime import datetime

class BanList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="banlist")
    async def banlist(self, ctx):
        lines = []
        for usn, data in all_bans():
            remaining = data["release_date"] - datetime.now()
            lines.append(f"{data['ign']} | {remaining}")

        if not lines:
            await ctx.send("✅ No temporary bans")
            return

        await ctx.send("🔴 Temp Bans:\n" + "\n".join(lines))

async def setup(bot):
    await bot.add_cog(BanList(bot))