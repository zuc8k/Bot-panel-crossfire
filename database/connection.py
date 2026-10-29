# database/connection.py
import pyodbc
from config.settings import DATABASES

connections: dict[str, pyodbc.Connection | None] = {}
cursors: dict[str, pyodbc.Cursor | None] = {}


def connect_all() -> None:
    """تهيئة الاتصال بجميع قواعد البيانات المحددة في الإعدادات."""
    print("🔌 Connecting to databases...")
    for key, cfg in DATABASES.items():
        try:
            conn = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={cfg['host']};"
                f"DATABASE={cfg['db']};"
                f"UID={cfg['user']};"
                f"PWD={cfg['password']};"
                f"TrustServerCertificate=yes;"
            )
            connections[key] = conn
            cursors[key] = conn.cursor()
            print(f"✅ Connected: {key}")
        except Exception as e:
            connections[key] = None
            cursors[key] = None
            print(f"❌ Failed {key}: {e}")


def close_all() -> None:
    """إغلاق جميع الاتصالات بأمان (يُستدعى عند إيقاف البوت)."""
    for key, conn in connections.items():
        if conn:
            try:
                conn.close()
                print(f"🔒 Closed connection: {key}")
            except Exception as e:
                print(f"⚠️ Error closing {key}: {e}")