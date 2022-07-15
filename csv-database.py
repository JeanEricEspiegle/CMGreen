import sqlite3
import csv

con = sqlite3.connect("shops_data.db")
cur = con.cursor()

a_file = open("WeedList.csv")
rows = csv.reader(a_file)
cur.executemany("INSERT INTO weedlist VALUES (?, ?)", rows)

cur.execute("SELECT * FROM weedlist")
print(cur.fetchall())
con.commit()
con.close()