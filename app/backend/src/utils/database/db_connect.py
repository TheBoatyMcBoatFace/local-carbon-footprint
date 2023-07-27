"""
db_connect.py

This module provides a Database class for connecting to an SQLite database.

Author: TheBoatyMcBoatFace
"""

import os
import sqlite3
from logger import logger


class Database:
    """
    Database class for connecting to an SQLite database.

    This class provides methods to establish a connection to an SQLite database and close the connection.

    Args:
        db_dir (str): Directory where the database file will be stored. Defaults to 'db'.
        db_file (str): Name of the database file. Defaults to 'carbon_footprint.sqlite'.
    """

    def __init__(self, db_dir='db', db_file='carbon_footprint.sqlite'):
        """
        Initialize a Database object.

        Args:
            db_dir (str): Directory where the database file will be stored. Defaults to 'db'.
            db_file (str): Name of the database file. Defaults to 'carbon_footprint.sqlite'.
        """
        # Ensure we are creating the database at project root
        base_dir = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))))))
        self.db_dir = os.path.join(base_dir, db_dir)
        self.db_file = db_file
        self.connection = None

    def get_connection(self):
        """
        Get a connection to the database.

        Returns:
            sqlite3.Connection: Connection to the database.
        """
        if not self.connection:
            if not os.path.exists(self.db_dir):
                os.makedirs(self.db_dir)
            self.connection = sqlite3.connect(os.path.join(self.db_dir, self.db_file))
        return self.connection

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()


# Test if database exists
if __name__ == "__main__":
    db = Database()
    conn = db.get_connection()
    logger.info(f"Database file created at {conn}")
    db.close()
