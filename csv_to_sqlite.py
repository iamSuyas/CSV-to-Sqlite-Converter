import csv
import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('jobfair.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    "index" INTEGER,
    email TEXT,
    name TEXT,
    phone_number TEXT,
    graduate TEXT,
    position TEXT,
    college TEXT,
    resume TEXT,
    status TEXT
)
''')

# Read CSV and insert data
with open('data.csv', 'r', encoding='utf-8') as file:
# with open('DWIT Job Fair Registration Form (Responses) - Form Responses 1.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    
    for row in csv_reader:
        # Map CSV columns to database columns
        cursor.execute('''
        INSERT INTO users ("index", email, name, phone_number, graduate, position, college, resume, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row[0],  # index
            row[2],  # Email
            row[1],  # Full Name
            row[3],  # Contact
            row[5],  # Graduated
            row[7],  # Interested Field
            row[4],  # College
            row[6],  # Upload Resume
            "not checked in"  # status
        ))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data transfer completed successfully!") 