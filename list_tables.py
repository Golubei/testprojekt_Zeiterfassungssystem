import sqlite3

DB_PATH = 'test.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Таблиці у базі:", tables)
conn.close()