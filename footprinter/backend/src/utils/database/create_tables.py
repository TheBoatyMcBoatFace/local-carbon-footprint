"""
create_tables.py

This script creates the necessary tables in the SQLite database for the Carbon Footprint project.

Author: TheBoatyMcBoatFace
"""

import sqlite3
import sys
from pathlib import Path

# Add the project root directory to the module search path
sys.path.append(str(Path(__file__).resolve().parents[5]))

from footprinter.backend.src.utils.logger import logger


def create_tables():
    """
    Create the necessary tables in the SQLite database.

    Returns:
        None
    """
    # Connect to SQLite database
    db_path = Path('db/carbon_footprint.sqlite')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create tables if they do not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS cpu_utilization (
            timestamp TEXT,
            utilization REAL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS system_info (
            machine_name TEXT,
            machine_type TEXT,
            cpu_info TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS geo_location (
            query TEXT,
            continent TEXT,
            country TEXT,
            region TEXT,
            city TEXT,
            district TEXT,
            zip TEXT,
            lat REAL,
            lon REAL,
            timezone TEXT,
            isp TEXT,
            org TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    logger.info("SQLite tables created successfully.")


if __name__ == '__main__':
    create_tables()
