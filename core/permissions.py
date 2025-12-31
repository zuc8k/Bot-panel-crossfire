# core/permissions.py

from core.ranks import OWNER, ADMIN, GUARD, MEMBER

PERMISSIONS = {
    "test":        [OWNER, ADMIN, GUARD, MEMBER],
    "myid":        [OWNER, ADMIN, GUARD, MEMBER],
    "helpme":      [OWNER, ADMIN, GUARD, MEMBER],
    "myrank":      [OWNER, ADMIN, GUARD, MEMBER],
    "checkrank":   [OWNER, ADMIN, GUARD, MEMBER],

    "add":         [OWNER],
    "remove":      [OWNER],
    "changerank":  [OWNER],
}

def has_permission(user_rank: str, command_name: str) -> bool:
    allowed = PERMISSIONS.get(command_name, [])
    return user_rank in allowed