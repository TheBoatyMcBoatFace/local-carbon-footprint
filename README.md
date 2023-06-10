/Users/Shared/GitHub/Orgs/CivicActions/local-carbon-footprint

https://www.cloudcarbonfootprint.org/docs/on-premise

Docker Vars

MachineType
    - server
    - laptop
    - desktop

MachineName
    - Default: Physical Host Name
    - Override with custom name

/Users/Shared/GitHub/Orgs/CivicActions/local-carbon-footprint/db/carbon_footprint.sqlite



import time
import sqlite3
import psutil
from .utils import logger

# Connect to SQLite database
conn = sqlite3.connect('db/carbon_footprint.sqlite')
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS cpu_utilization (
        timestamp TEXT,
        utilization REAL
    )
''')

while True:
    # Get current CPU utilization
    utilization = psutil.cpu_percent()

    # Get current timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Insert into database
    c.execute('INSERT INTO cpu_utilization VALUES (?, ?)', (timestamp, utilization))

    # Commit the transaction
    conn.commit()

    # Sleep for 60 seconds
    time.sleep(60)