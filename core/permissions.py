# core/permissions.py

from core.ranks import OWNER, ADMIN, GUARD, MEMBER

PERMISSIONS = {
    # Basic
    "test":   [OWNER, ADMIN, GUARD, MEMBER],
    "myid":   [OWNER, ADMIN, GUARD, MEMBER],
    "helpme": [OWNER, ADMIN, GUARD, MEMBER],

    # Owner/Admin
    "add":        [OWNER],
    "remove":     [OWNER],
    "changerank": [OWNER],

    # Game (هتتزود لاحقًا)
    "ban":   [OWNER, ADMIN, GUARD],
    "unban": [OWNER, ADMIN, GUARD],
}

def has_permission(user_rank: str, command_name: str) -> bool:
    allowed = PERMISSIONS.get(command_name, [])
    return user_rank in allowed