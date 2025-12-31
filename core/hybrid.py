# core/hybrid.py

import discord
from discord import app_commands
from discord.ext import commands

def hybrid_command(
    *,
    name: str,
    description: str = "",
):
    """
    Decorator يصنع Prefix + Slash من نفس الدالة
    """

    def decorator(func):

        # Prefix command
        prefix_cmd = commands.command(name=name)(func)

        # Slash command
        slash_cmd = app_commands.command(
            name=name,
            description=description
        )(func)

        # نجمع الاتنين
        func.__commands__ = {
            "prefix": prefix_cmd,
            "slash": slash_cmd
        }

        return func

    return decorator