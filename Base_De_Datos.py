
import sqlite3
DATABASE_NAME = "Clinica_Dental.db"


def obtener_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS Citas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
				telefono REAL NOT NULL,
				consulta TEXT NOT NULL
            )
            """
    ]
    db = obtener_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
