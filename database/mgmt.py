import sqlite3

def getShop(id):
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from shoplist where shopID = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("ID = ", row[0])
            print("Name  = ", row[2])
            print("Address  = ", row[3])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getShop(5)