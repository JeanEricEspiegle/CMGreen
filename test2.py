import sqlite3

conn = sqlite3.connect("shops_data.db")
cur = conn.cursor()
cur.execute("SELECT * FROM GreenDog")

rows = cur.fetchall()

for row in rows:
    print(row)