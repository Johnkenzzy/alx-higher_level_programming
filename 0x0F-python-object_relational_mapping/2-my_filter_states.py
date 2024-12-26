#!/usr/bin/python3
"""
Displays all argument values in the states table of the database hbtn_0e_0_usa
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
        WHERE name=%s\
        ORDER BY id ASC",
        ("{}".format(arg_list[3]),)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
