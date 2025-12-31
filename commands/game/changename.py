# commands/game/changename.py

from discord.ext import commands
from database.connection import cursors, connections

class ChangeName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changename")
    async def changename(self, ctx, old_ign: str = None, new_ign: str = None):
        if not old_ign or not new_ign:
            await ctx.send("❌ Usage: !changename <old_ign> <new_ign>")
            return

        cursor = cursors.get("CF_SA_GAME")
        conn = connections.get("CF_SA_GAME")

        cursor.execute(
            "UPDATE CF_USER SET NICK=? WHERE NICK=?",
            new_ign, old_ign
        )
        if cursor.rowcount == 0:
            await ctx.send("❌ Player not found")
            return

        conn.commit()
        await ctx.send(f"✏️ Name changed: `{old_ign}` → `{new_ign}`")

async def setup(bot):
    await bot.add_cog(ChangeName(bot))