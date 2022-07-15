import pandas as pd
import sqlite3


def shopWeed(id):
    match id:
        case 1:
            return " "
        case 2:
            return " "
        case 3:
            return " "
        case 4:
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM CannabisCafe")

            rows = cur.fetchall()
            return rows
        case 5:
            return " "
        case 6:
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM MavoixCoffee")

            rows = cur.fetchall()
            return rows
        case 7:
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM SPV")

            rows = cur.fetchall()
            return rows
        case 8:
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM MStudio")

            rows = cur.fetchall()
            return rows
        case 9:
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM GreenDog")

            rows = cur.fetchall()
            return rows
        case 10:
            return " "