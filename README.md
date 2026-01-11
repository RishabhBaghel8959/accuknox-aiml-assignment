# accuknox-aiml-assignment

# accuknox-aiml-assignment

# Accuknox AIML Assignment

This repository contains solutions to three problem statements involving API data handling, data processing & visualization, and CSV data import into a SQLite database using Python.

---

## 📁 Project Structure

accuknox-aiml-assignment  
├── Problem Statement 1  
│   ├── api_books_to_sqlite.py  
│   ├── Data Processing and Visualization.py  
│   ├── CSV Data Import to a Database.py  
│   ├── users.csv  
│   ├── books.db  
│   ├── users.db  
│  
├── Problem Statement 2  
│   ├── README.md  
│  
└── README.md  

---

## 🧩 Problem Statement 1: API Data Retrieval and Storage

**Objective:**  
Fetch book data from an external REST API, store it in a local SQLite database, and display the stored data.

**Approach:**
- Used Google Books REST API
- Parsed JSON fields: title, authors, publication year
- Stored data in SQLite (`books.db`)
- Displayed stored records

**Technologies Used:**  
Python, requests, sqlite3

---

## 📊 Problem Statement 2: Data Processing and Visualization

**Objective:**  
Fetch student test scores from an API, calculate the average score, and visualize the data using a bar chart.

**Approach:**
- Simulated API-style JSON data for reliability
- Extracted student names and scores
- Calculated average score
- Visualized scores using Matplotlib

**Technologies Used:**  
Python, matplotlib

---

## 📄 Problem Statement 3: CSV Data Import to Database

**Objective:**  
Read user data from a CSV file and insert it into a SQLite database.

**Approach:**
- Read `users.csv` using csv module
- Created SQLite database (`users.db`)
- Inserted records using parameterized SQL queries
- Verified stored data

**Technologies Used:**  
Python, csv, sqlite3

---

## ▶️ How to Run

1. Navigate to the required problem folder:
```bash
cd "Problem Statement 1"
