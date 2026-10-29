# main.py
import asyncio
from core.bot import bot
from core.checks import setup_checks
from core.loader import load_commands
from config.settings import TOKEN
from database.connection import connect_all, close_all


async def start() -> None:
    connect_all()
    setup_checks(bot)
    try:
        await load_commands(bot)
        await bot.start(TOKEN)
    finally:
        close_all()


if __name__ == "__main__":
    print("🚀 Starting bot (Hybrid Mode)...")
    asyncio.run(start())