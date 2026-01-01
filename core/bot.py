import discord
from discord.ext import commands, tasks

from core.ranks import load_ranks
from tasks.daily_report_task import send_daily_report

# ================== INTENTS ==================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ================== BOT ==================
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None  # ❌ تعطيل الـ Default Help نهائيًا
)

# ================== TASKS ==================
@tasks.loop(hours=24)
async def daily_admin_report():
    try:
        await send_daily_report(bot)
        print("📊 Daily admin report sent")
    except Exception as e:
        print(f"❌ Daily report failed: {e}")

@daily_admin_report.before_loop
async def before_daily_report():
    await bot.wait_until_ready()

# ================== EVENTS ==================
@bot.event
async def on_ready():
    # تحميل الرتب
    load_ranks()

    # تشغيل التقرير اليومي
    if not daily_admin_report.is_running():
        daily_admin_report.start()
        print("⏰ Daily admin report task started")

    # مزامنة أوامر السلاش
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Slash sync failed: {e}")

    print(f"✅ Bot Online as {bot.user}")
    print(f"🆔 Bot ID: {bot.user.id}")