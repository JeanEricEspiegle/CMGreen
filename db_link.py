import sqlite3
import pandas as pd
import base64

def getShops():
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        print("Connected to SQLite")

        sql_query = pd.read_sql_query ('''SELECT * FROM shoplist''', sqliteConnection)

        df = pd.DataFrame(sql_query, columns = ['shopID', 'photo', 'name', 'address'])

        print(df.name + df.address)

        pic = df.photo[1]
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

    return (pic)

shops = getShops()
