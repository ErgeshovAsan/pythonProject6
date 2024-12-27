import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS complaints(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    complaint TEXT
                )
            """)
            conn.commit()


    def save_complaint(self, data: dict):
        with sqlite3.connect("db.sqlite3") as conn:
            conn.execute("""
                INSERT INTO complaints (name, phone, complaint)
                VALUES (?, ?, ?)
                """,
                (data["name"], data["phone"], data["complaint"]))



database = Database("db.sqlite3")