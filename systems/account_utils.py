# systems/account_utils.py

import random
import string
import hashlib

def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def hash_password_md5(password: str) -> str:
    # مطابق للنظام القديم (هيتغيّر لاحقًا لأقوى)
    return hashlib.md5(password.encode("utf-8")).hexdigest()