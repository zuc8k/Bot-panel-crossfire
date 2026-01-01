import discord
from services.daily_report_service import get_daily_admin_report
from config.settings import ADMIN_LOG_CHANNEL_ID

async def send_daily_report(bot):
    channel = bot.get_channel(ADMIN_LOG_CHANNEL_ID)
    rows = get_daily_admin_report()

    if not rows or not channel:
        return

    embed = discord.Embed(
        title="📊 Daily Admin Report",
        color=0x1ABC9C
    )

    data = {}
    for admin, action, count in rows:
        data.setdefault(admin, [])
        data[admin].append(f"{action}: {count}")

    for admin, actions in data.items():
        embed.add_field(
            name=admin,
            value="\n".join(actions),
            inline=False
        )

    await channel.send(embed=embed)