from sys import argv, exit
import sqlite3
import csv

if len(argv) != 2:
    print('Usage: python import.py characters.csv')
    exit(1)

with open(argv[1], 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    db_conn = sqlite3.connect("students.db")
    db = db_conn.cursor()
    query = ("INSERT INTO students (first, middle, last, house, birth) VALUES( ?, ?, ?, ?, ?)")

    for row in csv_reader:
        if len(row["name"].split()) == 2:
            data = [row["name"].split()[0], None, row["name"].split()[1],row['house'], row['birth']]
            db.execute(query,data)
        else:
            data = [row["name"].split()[0], row["name"].split()[1], row["name"].split()[2],row['house'], row['birth']]            
            db.execute(query,data)
        
        db_conn.commit()
    
    db.close()
    db_conn.close()
