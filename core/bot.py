import discord
from discord.ext import commands
from core.ranks import load_ranks

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

# ================== EVENTS ==================
@bot.event
async def on_ready():
    # تحميل الرتب
    load_ranks()

    # مزامنة أوامر السلاش
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Slash sync failed: {e}")

    print(f"✅ Bot Online as {bot.user}")
    print(f"🆔 Bot ID: {bot.user.id}")