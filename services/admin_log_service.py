# services/admin_log_service.py

import discord
from config.settings import ADMIN_LOG_CHANNEL_ID
from core.ranks import RANK_NAMES, get_user_rank

async def send_admin_log(
    bot,
    *,
    action: str,
    admin,
    target: str = "-",
    details: str = "-"
):
    if not ADMIN_LOG_CHANNEL_ID:
        return

    channel = bot.get_channel(ADMIN_LOG_CHANNEL_ID)
    if not channel:
        return

    rank = get_user_rank(admin.id)
    rank_name = RANK_NAMES.get(rank, rank)

    embed = discord.Embed(
        title="📋 Admin Action Log",
        color=0xE74C3C
    )

    embed.add_field(name="Action", value=action, inline=False)
    embed.add_field(
        name="Admin",
        value=f"{admin.mention}\n{rank_name}",
        inline=True
    )
    embed.add_field(name="Target", value=target, inline=True)
    embed.add_field(name="Details", value=details, inline=False)

    await channel.send(embed=embed)