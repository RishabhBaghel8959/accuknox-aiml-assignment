import csv
import sqlite3
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full path to users.csv
CSV_FILE_PATH = os.path.join(BASE_DIR, "users.csv")

print("Looking for CSV at:", CSV_FILE_PATH)

# Step 1: Connect to SQLite database (in same folder)
DB_PATH = os.path.join(BASE_DIR, "users.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Step 2: Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Step 3: Read CSV and insert data
with open(CSV_FILE_PATH, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

conn.commit()
conn.close()

print("✅ CSV data imported successfully into SQLite database.")
