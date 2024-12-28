#!/usr/bin/python3
import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
except MySQLdb.Error as e:
    print("%s" % e)
try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books")
    rows = cur.fetchall()
except MySQLdb.Error as e:
    print(e)
for row in rows:
    for col in row:
        print(col)
    print()
cur.close()
conn.close()
