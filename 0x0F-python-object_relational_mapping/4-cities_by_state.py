#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    arg_list = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=arg_list[0],
        passwd=arg_list[1], db=arg_list[2], charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name AS state_name\
        FROM cities\
        JOIN states ON cities.state_id = states.id\
        ORDER BY id ASC"
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
