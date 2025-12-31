# services/help_service.py

from core.permissions import PERMISSIONS
from core.ranks import RANK_NAMES

def build_help_menu(user_rank: str):
    menu = {}

    for command, allowed_ranks in PERMISSIONS.items():
        if user_rank in allowed_ranks:
            category = get_category(command)
            menu.setdefault(category, []).append(command)

    return menu


def get_category(command_name: str) -> str:
    if command_name in ["ban", "unban", "checkhold"]:
        return "🔨 Ban System"
    if command_name in ["addgp", "checkgp", "gplogs"]:
        return "💰 GP System"
    if command_name in ["addzp", "checkzp"]:
        return "💎 ZP System"
    if command_name in ["changepass", "genpass", "changename", "checkaccount"]:
        return "👤 Account"
    if command_name in ["help", "test"]:
        return "ℹ️ General"
    return "📦 Other"