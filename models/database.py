import sqlite3
from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __new__(cls, db="./database/user.db"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.conn = sqlite3.connect(db, check_same_thread=False)
                cls._instance.conn.row_factory = sqlite3.Row

        return cls._instance

    def execute(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()
    
    def commit(self):
        self.conn.commit()
