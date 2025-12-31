# systems/log_utils.py

import random
from datetime import datetime

def generate_log_id():
    return random.randint(100000, 999999)

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")