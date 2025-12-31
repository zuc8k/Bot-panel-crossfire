# services/rank_service.py

import json
from pathlib import Path

RANKS_FILE = Path("data/ranks.json")

def load_ranks_file():
    if not RANKS_FILE.exists():
        return {}
    with open(RANKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_ranks_file(data: dict):
    with open(RANKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_rank(user_id: int, rank: str):
    data = load_ranks_file()
    data[str(user_id)] = rank
    save_ranks_file(data)

def remove_rank(user_id: int):
    data = load_ranks_file()
    if str(user_id) in data:
        del data[str(user_id)]
        save_ranks_file(data)
        return True
    return False