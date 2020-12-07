import mysql.connector as mysql
from mysql.connector import Error
import sql_query
import sys

config = {
    'user': 'root',
    'password':'',
    'host': '127.0.0.1',
} 

#Create Table
try:
    db = mysql.connect(**config)
    if db.is_connected():
        print("Connected to MySQL Server")
        cursor = db.cursor()
        cursor.execute(sql_query.create_database)
        cursor.execute(sql_query.show_db)
        cursor.fetchall()
        cursor.execute("USE VALUESTOCKS")
except Error as e:
    print("Error while connecting to MySQL", e)


