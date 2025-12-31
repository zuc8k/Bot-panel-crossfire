# core/bot.py

import discord
from discord.ext import commands
from core.ranks import load_ranks

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    load_ranks()
    print(f"✅ Bot Online as {bot.user}")
    print(f"🆔 Bot ID: {bot.user.id}")