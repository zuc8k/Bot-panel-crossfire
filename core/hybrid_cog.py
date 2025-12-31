# core/hybrid_cog.py

from discord.ext import commands
import discord

class HybridCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        for attr in dir(self):
            method = getattr(self, attr)
            if hasattr(method, "__commands__"):
                cmds = method.__commands__

                # Prefix
                self.bot.add_command(cmds["prefix"])

                # Slash
                self.bot.tree.add_command(cmds["slash"])