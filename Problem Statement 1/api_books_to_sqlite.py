import requests
import sqlite3


API_URL = "https://www.googleapis.com/books/v1/volumes?q=python"
response = requests.get(API_URL)

items = response.json().get("items", []) if response.status_code == 200 else []



conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    author TEXT,
    year TEXT
)
""")



for item in items:
    info = item.get("volumeInfo", {})
    title = info.get("title", "Unknown")
    authors = ", ".join(info.get("authors", ["Unknown"]))
    published_date = info.get("publishedDate", "N/A")
    year = published_date[:4] if published_date != "N/A" else "N/A"

    cursor.execute("""
        INSERT OR IGNORE INTO books (title, author, year)
        VALUES (?, ?, ?)
    """, (title, authors, year))

conn.commit()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
