# commands/help/help.py

from discord.ext import commands
from services.help_service import build_help_menu
from core.ranks import get_user_rank, RANK_NAMES

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        rank = get_user_rank(ctx.author.id)
        rank_name = RANK_NAMES.get(rank, rank)

        menu = build_help_menu(rank)

        message = f"📖 **Help Menu**\n"
        message += f"👤 Rank: **{rank_name}**\n\n"

        for category, commands_list in menu.items():
            message += f"**{category}**\n"
            for cmd in commands_list:
                message += f"• `!{cmd}`\n"
            message += "\n"

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Help(bot))