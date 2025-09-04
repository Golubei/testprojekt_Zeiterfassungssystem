import sqlite3
import csv

DB_PATH = 'test.db'
TABLE_NAME = 'zeitbuchungen'
CSV_PATH = 'zeitbuchungen_export.csv'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")
rows = cursor.fetchall()
col_names = [description[0] for description in cursor.description]

with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(col_names)
    writer.writerows(rows)

print(f"Дані експортовано у {CSV_PATH}")
conn.close()