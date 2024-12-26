#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    arg_list = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=arg_list[0],
        passwd=arg_list[1], db=arg_list[2], charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states\
        WHERE BINARY states.name LIKE %s\
        ORDER BY id ASC",
        ('N%',)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
