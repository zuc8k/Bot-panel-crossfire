# core/permissions.py

from core.ranks import OWNER, ADMIN, GUARD, MEMBER

PERMISSIONS = {
    # Basic
    "help":        [OWNER, ADMIN, GUARD, MEMBER],
    "test":        [OWNER, ADMIN, GUARD, MEMBER],

    # Account
    "checkaccount":[OWNER, ADMIN, GUARD],
    "changepass":  [OWNER, ADMIN],
    "genpass":     [OWNER, ADMIN],
    "changename":  [OWNER, ADMIN],

    # GP
    "checkgp":     [OWNER, ADMIN, GUARD],
    "addgp":       [OWNER, ADMIN],

    # ZP
    "checkzp":     [OWNER, ADMIN, GUARD],
    "addzp":       [OWNER, ADMIN],

    # BAN / HOLD
    "ban":         [OWNER, ADMIN, GUARD],
    "unban":       [OWNER, ADMIN],
    "checkhold":   [OWNER, ADMIN, GUARD],

    # Logs
    "logs":        [OWNER, ADMIN],
    "mylogs":      [OWNER, ADMIN, GUARD],
}

def has_permission(user_rank: str, command_name: str) -> bool:
    allowed = PERMISSIONS.get(command_name, [])
    return user_rank in allowed