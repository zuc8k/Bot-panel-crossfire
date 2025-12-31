# core/slash.py

import discord
from discord.ext import commands

class SlashSync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            synced = await self.bot.tree.sync()
            print(f"✅ Slash Commands Synced: {len(synced)}")
        except Exception as e:
            print(f"❌ Slash Sync Error: {e}")

async def setup(bot):
    await bot.add_cog(SlashSync(bot))