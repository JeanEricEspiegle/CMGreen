import csv, sqlite3


sqliteConnection = sqlite3.connect('shops_data.db')
sqlite_create_table_query = '''CREATE TABLE WeedConnection (
                            name TEXT PRIMARY KEY,
                            price INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            thc INTEGER NOT NULL);'''

cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()
print("SQLite table created")
cursor.close()



con = sqlite3.connect('shops_data.db')
cur = con.cursor()

a_file = open("WeedConn.csv")
rows = csv.reader(a_file)
cur.executemany("INSERT INTO WeedConnection  VALUES (?,?,?,?)", rows)

cur.execute("SELECT * FROM WeedConnection ")
print(cur.fetchall())
con.commit()
con.close()