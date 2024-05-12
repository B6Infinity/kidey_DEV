import os
from datetime import datetime

DB_FROM = ''
DB_TO = '..\\DB\\'
CHANGELOG = DB_TO + 'change.log'
PREVIOUS_SNAPSHOTS = DB_TO + 'previous_snapshots\\'

BACKUP_DB = "backup_db.sqlite3"

time_of_op = str(datetime.now()).replace(":", '-').replace('.', '')

def add_to_log(text):
    with open(CHANGELOG, 'a+') as f:
        f.write(f"\n[{time_of_op}]:\t{text}")

# Windows only

# Back up previous_snapshot
# Add to changelog
# Add recent backup

OLD_DB_NAME = f"\"{PREVIOUS_SNAPSHOTS}old_db_{time_of_op}.sqlite3\""

try:
    os.system(f'MOVE {DB_TO}{BACKUP_DB} {OLD_DB_NAME}')
except Exception as e:
    print("Could not find 'db.sqlite3'... Skipping...")
    add_to_log("Could not find previous backup")
    

os.system(f'COPY db.sqlite3 {DB_TO}{BACKUP_DB}')
add_to_log(f"Backed up {OLD_DB_NAME}.")