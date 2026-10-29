# systems/ban_utils.py
from datetime import datetime, timedelta
from typing import Optional


def parse_duration(duration: str) -> Optional[datetime]:
    """
    تحويل مدة الحظر النصية إلى تاريخ انتهاء.
    الصيغ المدعومة: "perma" (دائم)، "1h" (ساعة)، "2d" (يوم).
    تعيد None إذا كانت المدة دائمة أو غير صالحة.
    """
    if not duration or not isinstance(duration, str):
        return None

    duration = duration.strip().lower()
    if duration == "perma":
        return None

    if len(duration) < 2:
        return None

    unit = duration[-1]
    value_str = duration[:-1]

    try:
        value = int(value_str)
    except ValueError:
        return None

    if value <= 0:
        return None

    if unit == "h":
        return datetime.now() + timedelta(hours=value)
    elif unit == "d":
        return datetime.now() + timedelta(days=value)

    return None