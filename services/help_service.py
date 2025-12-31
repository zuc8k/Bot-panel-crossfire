# services/help_service.py

from core.permissions import PERMISSIONS

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

def get_available_categories(user_rank: str):
    available = {}

    for key, data in CATEGORIES.items():
        allowed_cmds = []
        for cmd in data["commands"]:
            if user_rank in PERMISSIONS.get(cmd, []):
                allowed_cmds.append(cmd)

        if allowed_cmds:
            available[key] = {
                "label": data["label"],
                "commands": allowed_cmds
            }

    return available