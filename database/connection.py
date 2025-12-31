import pyodbc
from config.database import SERVER, USERNAME, PASSWORD, DATABASES

connections = {}
cursors = {}

def connect_all():
    for key, db in DATABASES.items():
        try:
            conn = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={SERVER};DATABASE={db};"
                f"UID={USERNAME};PWD={PASSWORD};"
                "TrustServerCertificate=yes;"
            )
            connections[key] = conn
            cursors[key] = conn.cursor()
            print(f"✅ Connected: {key}")
        except Exception as e:
            connections[key] = None
            cursors[key] = None
            print(f"❌ DB Error {key}: {e}")

connect_all()