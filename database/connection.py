import pyodbc
from config.database import DB_SERVER, DB_USER, DB_PASS, DATABASES

connections = {}
cursors = {}

def connect_all():
    print("🔌 Connecting to databases...")
    for key, db_name in DATABASES.items():
        try:
            conn = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={DB_SERVER};"
                f"DATABASE={db_name};"
                f"UID={DB_USER};"
                f"PWD={DB_PASS};"
                f"TrustServerCertificate=yes;"
            )
            connections[key] = conn
            cursors[key] = conn.cursor()
            print(f"✅ Connected: {key}")
        except Exception as e:
            connections[key] = None
            cursors[key] = None
            print(f"❌ Failed {key}: {e}")