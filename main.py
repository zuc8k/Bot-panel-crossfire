from core.bot import bot
from config.settings import TOKEN
from database.connection import connect_all

if __name__ == "__main__":
    print("🚀 Starting bot...")
    connect_all()
    bot.run(TOKEN)