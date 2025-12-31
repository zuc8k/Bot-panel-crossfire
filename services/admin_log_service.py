from database.connection import cursors, connections
from config.settings import ADMIN_LOG_CHANNEL_ID
from core.ranks import get_user_rank, RANK_NAMES
import discord

async def send_admin_log(
    bot,
    *,
    action: str,
    admin,
    target: str = "-",
    details: str = "-"
):
    # -------- Discord Log --------
    if ADMIN_LOG_CHANNEL_ID:
        channel = bot.get_channel(ADMIN_LOG_CHANNEL_ID)
        if channel:
            rank = get_user_rank(admin.id)
            rank_name = RANK_NAMES.get(rank, rank)

            embed = discord.Embed(
                title="📋 Admin Action Log",
                color=0xE67E22
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

    # -------- Database Log --------
    cursor = cursors.get("CF_SA_GAME")
    conn = connections.get("CF_SA_GAME")

    if cursor and conn:
        cursor.execute(
            """
            INSERT INTO CF_ADMIN_LOG
            (ADMIN_ID, ADMIN_NAME, ACTION, TARGET, DETAILS)
            VALUES (?, ?, ?, ?, ?)
            """,
            admin.id,
            str(admin),
            action,
            target,
            details
        )
        conn.commit()