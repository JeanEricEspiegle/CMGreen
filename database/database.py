import sqlite3
import csv
import numpy as np
import pandas as pd

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(shopID, photo, name, address):
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO shoplist
                                  (shopID, photo, name, address) VALUES (?, ?, ?, ?)"""

        shopPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (shopID, shopPhoto, name, address)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB(6, "mavoixcoffee.jpg", "Mavoix Coffee", "18 Rachadamnoen Rd Soi 1, Tambon Si Phum, Mueang Chiang Mai District, Chiang Mai 50300")
