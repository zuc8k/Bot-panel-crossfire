# systems/ban_utils.py

from datetime import datetime, timedelta

def parse_duration(duration: str):
    if duration == "perma":
        return None

    unit = duration[-1].lower()
    value = int(duration[:-1])

    if unit == "h":
        return datetime.now() + timedelta(hours=value)
    elif unit == "d":
        return datetime.now() + timedelta(days=value)

    return None