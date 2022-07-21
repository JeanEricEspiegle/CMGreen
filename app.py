import os
import sqlite3
import pandas as pd


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
    desc = getShopDesc()
    shopID=0
    return render_template('shops.html', len=len(shopnames), shopname=shopnames, photo =images, address= shopaddy, description = desc)


@app.route('/shop/<ID>')
def displayShop(ID: int):
    info = getShopInfo(ID)
    weed = getShopWeed(ID)
    
    return render_template('shop.html', len=len(weed), information= info, cannalist = weed)

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
def getShopDesc():
    try:
        sqliteConnection = sqlite3.connect('shops_data.db')
        print("Connected to SQLite")

        sql_query = pd.read_sql_query ('''SELECT * FROM shoplist''', sqliteConnection)

        df = pd.DataFrame(sql_query, columns = ['shopID', 'name', 'address', 'imgurl', 'description'])

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    print(df)
    names = df.description
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
            desc = row[4]
            info = [shopID,name,addy,url, desc]
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

        if id == "High Queen CNX":
            return " "
        elif id == "Deep Green @ Deejai Garden":
            return " "
        elif id == "Rasta Cafe":
            return " "
        elif id == "Cannabis Cafe":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM CannabisCafe")
            rows = cur.fetchall()
            return rows
        elif id == "Shogun Minimart":
            return " "
        elif id == "Mavoix Coffee":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM MavoixCoffee")
            rows = cur.fetchall()
            return rows
        elif id == "SPV Cafe":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM SPV")
            rows = cur.fetchall()
            return rows
        elif id == "M Studio Cannabis Dispensary":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM MStudio")
            rows = cur.fetchall()
            return rows
        elif id == "Green Dog":
            conn = sqlite3.connect("shops_data.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM GreenDog")
            rows = cur.fetchall()
            return rows
        elif id == "420 Cannabis Cafe Bar & Restaurant":
            return " "