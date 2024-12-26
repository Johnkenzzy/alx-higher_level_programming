#!/usr/bin/python3
"""
Takes in the name of state as argument and
lists all cities of the state from database hbtn_0e_4_usa
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
        "SELECT cities.id, cities.name\
        FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY id ASC",
        (arg_list[3],)
        )
    rows = cur.fetchall()
    print(", ".join([row[1] for row in rows]))
    cur.close()
    conn.close()
