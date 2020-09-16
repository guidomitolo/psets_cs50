from sys import argv, exit
import sqlite3
import csv

if len(argv) != 2:
    print('Usage: python roster.py [house]')
    exit(1)

house = argv[1]

db_conn = sqlite3.connect("students.db")
db = db_conn.cursor()
query = (f"SELECT first, middle, last, birth FROM students WHERE house = \"{house}\" ORDER BY last, first")

db.execute(query)
data = db.fetchall()

for row in data:
    if row[1] == None:
        print(f"{row[0]} {row[2]}, born {row[-1]}")
    else:
        print(f"{row[0]} {row[1]} {row[2]}, born {row[-1]}")