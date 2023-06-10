# database.py
import os
import sqlite3
from logger import logger


class Database:
    def __init__(self, db_dir='db', db_file='carbon_footprint.sqlite'):
        # Ensure we are creating the database at project root
        base_dir = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))))
        self.db_dir = os.path.join(base_dir, db_dir)
        self.db_file = db_file
        self.connection = None

    def get_connection(self):
        if not self.connection:
            if not os.path.exists(self.db_dir):
                os.makedirs(self.db_dir)
            self.connection = sqlite3.connect(os.path.join(self.db_dir, self.db_file))
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()


# Test if database exists
if __name__ == "__main__":
    db = Database()
    conn = db.get_connection()
    logger.info(f"Database file created at {conn}")
    db.close()
