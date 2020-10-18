import sqlite3
from base.settings import DATABASE, SQL_REQUEST

con = sqlite3.connect(DATABASE)
cur = con.cursor()

with open(SQL_REQUEST, 'r') as file:
    text = file.read()

cur.executescript(text)
cur.close()
con.close()
