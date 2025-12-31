# commands/zp/checkzp.py

from discord.ext import commands
from database.connection import cursors
from systems.zp_utils import format_zp

class CheckZP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="checkzp")
    async def checkzp(self, ctx, ign: str = None):
        if not ign:
            await ctx.send("❌ Usage: !checkzp <IGN>")
            return

        cursor_game = cursors.get("CF_SA_GAME")
        cursor_bill = cursors.get("G4BOX_SA_BILL_DB")

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
        zp = cash_row[0] if cash_row else 0

        await ctx.send(
            f"💎 ZP Balance\n"
            f"Player: `{ign}`\n"
            f"ZP: {format_zp(zp)}"
        )

async def setup(bot):
    await bot.add_cog(CheckZP(bot))