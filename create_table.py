import sqlite3

connection=sqlite3.connect('test.db')
cursor=connection.cursor()

add_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY ,username text,password text)"
add_table1="CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name text,price real )"

cursor.execute(add_table)
cursor.execute(add_table1)

connection.commit()
connection.close()