# services/zp_service.py

from database.connection import cursors, connections

def get_user_usn(ign: str):
    cursor_game = cursors.get("CF_SA_GAME")
    cursor_game.execute(
        "SELECT USN, NICK FROM CF_USER WHERE NICK=?",
        ign
    )
    return cursor_game.fetchone()

def check_zp_logic(ign: str):
    row = get_user_usn(ign)
    if not row:
        return None

    usn, nick = row
    cursor_bill = cursors.get("G4BOX_SA_BILL_DB")
    cursor_bill.execute(
        "SELECT Cash FROM TAccountCashMst WHERE UserNo=?",
        usn
    )
    cash_row = cursor_bill.fetchone()
    zp = cash_row[0] if cash_row else 0

    return {
        "usn": usn,
        "nick": nick,
        "zp": zp
    }

def add_zp_logic(ign: str, amount: int):
    row = get_user_usn(ign)
    if not row:
        return None

    usn, nick = row
    cursor_bill = cursors.get("G4BOX_SA_BILL_DB")
    conn_bill = connections.get("G4BOX_SA_BILL_DB")

    cursor_bill.execute(
        "SELECT Cash FROM TAccountCashMst WHERE UserNo=?",
        usn
    )
    cash_row = cursor_bill.fetchone()
    old_zp = cash_row[0] if cash_row else 0
    new_zp = old_zp + amount

    if cash_row:
        cursor_bill.execute(
            "UPDATE TAccountCashMst SET Cash=? WHERE UserNo=?",
            new_zp, usn
        )
    else:
        cursor_bill.execute(
            "INSERT INTO TAccountCashMst (UserNo, Cash) VALUES (?, ?)",
            usn, new_zp
        )

    conn_bill.commit()

    return {
        "usn": usn,
        "nick": nick,
        "old_zp": old_zp,
        "new_zp": new_zp,
        "added": amount
    }