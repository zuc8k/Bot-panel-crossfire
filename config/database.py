# config/database.py
"""
تم توحيد إعدادات قاعدة البيانات في config/settings.py.
هذا الملف موجود للتوافق الخلفي فقط ويعيد تصدير القيم من settings.
يُفضّل عدم استخدامه في الكود الجديد.
"""

from config.settings import DATABASES

# للتوافق مع أي كود قديم يستورد DB_SERVER أو DB_USER أو DB_PASS
# (لم يعد هناك متغيرات عامة، لذا نتركها فارغة أو نحذفها)
__all__ = ["DATABASES"]