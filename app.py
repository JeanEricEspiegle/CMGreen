import os
import sqlite3
import pandas as pd
from base64 import b64encode
from PIL import Image
from io import BytesIO
import io
import codecs


from flask import Flask
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, Response, send_file)

path = "C:/Users/jee30/Desktop/CM Greens/instance"
# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='super secret key',
    DATABASE=os.path.join(path, 'shops.sqlite'),
)

# a simple page that says hello
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/photo')
def getPhoto():
    return Response(images, mimetype='image/jpeg')


@app.route('/shops', methods=['GET','POST'])
def shops():
    shopnames = getShopNames()
    shopaddy = getShopAdd()
    images = getShopPhoto()
    print(images)
    print(shopnames)
    print(shopaddy)
    shopID=0
    for i in images:
        shopID = shopID+1

    return render_template('shopcards.html', len=len(shopnames), shopname=shopnames, photo =images, address= shopaddy, ID= shopID)


@app.route('/shop/<ID>')
def displayShop(ID: int):
    info = getShopInfo(ID)
    weed = getShopWeed(ID)
    return render_template('shop.html')

##############################################################################

##############################################################################
def getShopNames():
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        print("Connected to SQLite")

        sql_query = pd.read_sql_query ('''SELECT * FROM shoplist''', sqliteConnection)

        df = pd.DataFrame(sql_query, columns = ['shopID', 'name', 'address', 'imgurl'])

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    names = df.name
    return (names)
##############################################################################
def getShopPhoto():
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        print("Connected to SQLite")

        sql_query = pd.read_sql_query ('''SELECT * FROM shoplist''', sqliteConnection)

        df = pd.DataFrame(sql_query, columns = ['shopID', 'name', 'address', 'imgurl'])

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    print(df.imgurl)
    names = df.imgurl
    return (names)
##############################################################################
def getShopAdd():
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        print("Connected to SQLite")

        sql_query = pd.read_sql_query ('''SELECT * FROM shoplist''', sqliteConnection)

        df = pd.DataFrame(sql_query, columns = ['shopID', 'name', 'address', 'imgurl'])

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    names = df.address
    return (names)
##############################################################################
def getShopInfo(id):
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from shoplist where name = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            shopID =  row[0]
            name  =  row[1]
            addy  = row[2]
            url  =  row[3]
            info = [shopID,name,addy,url]
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return(info)
##############################################################################
def getShopWeed(id):
    match id:
        case "High Queen CNX":
            return " "
        case "Deep Green @ Deejai Garden":
            return " "
        case "Rasta Cafe":
            return " "
        case "Cannabis Cafe":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM CannabisCafe")

            rows = cur.fetchall()
            return rows
        case "Shogun Minimart":
            return " "
        case "Mavoix Coffee":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM MavoixCoffee")

            rows = cur.fetchall()
            return rows
        case "SPV Cafe":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM SPV")

            rows = cur.fetchall()
            return rows
        case "M Studio Cannabis Dispensary":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM MStudio")

            rows = cur.fetchall()
            return rows
        case "Green Dog":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM GreenDog")

            rows = cur.fetchall()
            return rows
        case "420 Cannabis Cafe Bar & Restaurant":
            return " "