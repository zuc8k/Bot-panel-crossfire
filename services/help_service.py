from core.permissions import PERMISSIONS
from core.ranks import RANK_NAMES

# ==============================
# HELP CATEGORIES
# ==============================

CATEGORIES = {
    "general": {
        "label": "📖 General",
        "commands": ["help", "test"]
    },
    "account": {
        "label": "👤 Account",
        "commands": ["checkaccount", "changepass", "genpass", "changename"]
    },
    "gp": {
        "label": "💰 GP System",
        "commands": ["checkgp", "addgp", "gplogs"]
    },
    "zp": {
        "label": "💎 ZP System",
        "commands": ["checkzp", "addzp"]
    },
    "ban": {
        "label": "🔨 Ban System",
        "commands": ["ban", "unban", "checkhold"]
    }
}

# ==============================
# FILTER COMMANDS BY RANK
# ==============================

def get_available_categories(user_rank: str):
    """
    Returns categories and commands available for this rank
    """
    available = {}

    for key, data in CATEGORIES.items():
        allowed_cmds = []

        for cmd in data["commands"]:
            # لو الأمر مش محتاج صلاحيات
            if cmd not in PERMISSIONS:
                allowed_cmds.append(cmd)
                continue

            # لو الرتبة مسموح لها
            if user_rank in PERMISSIONS.get(cmd, []):
                allowed_cmds.append(cmd)

        if allowed_cmds:
            available[key] = {
                "label": data["label"],
                "commands": allowed_cmds
            }

    return available


# ==============================
# BUILD HELP MENU (FIXED)
# ==============================

def build_help_menu(user_rank: str) -> dict:
    """
    Builds structured help menu for prefix & slash
    """
    categories = get_available_categories(user_rank)

    menu = {
        "rank": RANK_NAMES.get(user_rank, user_rank),
        "categories": []
    }

    for key, data in categories.items():
        menu["categories"].append({
            "key": key,
            "label": data["label"],
            "commands": data["commands"]
        })

    return menu