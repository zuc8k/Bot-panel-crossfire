# commands/info/test.py

from discord.ext import commands

class TestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send("✅ Bot is working")

async def setup(bot):
    await bot.add_cog(TestCommand(bot))