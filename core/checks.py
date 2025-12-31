# core/checks.py

import discord
from discord.ext import commands

from config.settings import ALLOWED_IDS, ALLOWED_CHANNELS
from core.ranks import get_user_rank
from core.permissions import has_permission

def setup_checks(bot: commands.Bot):

    @bot.check
    async def channel_check(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return True
        if not ALLOWED_CHANNELS:
            return True
        return ctx.channel.id in ALLOWED_CHANNELS

    @bot.check
    async def allowed_user_check(ctx):
        return ctx.author.id in ALLOWED_IDS

    @bot.check
    async def permission_check(ctx):
        if not ctx.command:
            return True
        rank = get_user_rank(ctx.author.id)
        return has_permission(rank, ctx.command.name)