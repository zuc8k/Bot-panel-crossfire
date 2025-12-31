from core.bot import bot
from core.checks import setup_checks
from config.settings import TOKEN
from database.connection import connect_all

if __name__ == "__main__":
    print("🚀 Starting bot...")

    # Connect to databases
    connect_all()

    # Setup global checks (channels / allowed users / permissions)
    setup_checks(bot)

    # Run bot
    bot.run(TOKEN)