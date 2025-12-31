from core.bot import bot
from config.settings import TOKEN
from tasks.auto_unban import start_auto_unban

if __name__ == "__main__":
    start_auto_unban(bot)
    bot.run(TOKEN)