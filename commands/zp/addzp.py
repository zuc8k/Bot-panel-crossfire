# commands/zp/addzp.py

from discord.ext import commands
from database.connection import cursors, connections
from systems.zp_utils import format_zp
import random

class AddZP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addzp")
    async def addzp(self, ctx, ign: str = None, amount: int = None, *, reason: str = None):
        if not ign or amount is None or not reason:
            await ctx.send("❌ Usage: !addzp <IGN> <amount> <reason>")
            return

        cursor_game = cursors.get("CF_SA_GAME")
        cursor_bill = cursors.get("G4BOX_SA_BILL_DB")
        conn_bill = connections.get("G4BOX_SA_BILL_DB")

        cursor_game.execute(
            "SELECT USN FROM CF_USER WHERE NICK=?",
            ign
        )
        row = cursor_game.fetchone()

        if not row:
            await ctx.send("❌ Player not found")
            return

        usn = row[0]

        cursor_bill.execute(
            "SELECT Cash FROM TAccountCashMst WHERE UserNo=?",
            usn
        )
        cash_row = cursor_bill.fetchone()
        old_cash = cash_row[0] if cash_row else 0

        new_cash = old_cash + amount

        if cash_row:
            cursor_bill.execute(
                "UPDATE TAccountCashMst SET Cash=? WHERE UserNo=?",
                new_cash, usn
            )
        else:
            cursor_bill.execute(
                "INSERT INTO TAccountCashMst (UserNo, Cash) VALUES (?, ?)",
                usn, new_cash
            )

        conn_bill.commit()

        await ctx.send(
            f"💎 ZP Added Successfully\n"
            f"Player: `{ign}`\n"
            f"Old ZP: {format_zp(old_cash)}\n"
            f"Added: {format_zp(amount)}\n"
            f"New ZP: {format_zp(new_cash)}\n"
            f"Reason: {reason}"
        )

async def setup(bot):
    await bot.add_cog(AddZP(bot))