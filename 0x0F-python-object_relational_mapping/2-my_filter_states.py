#!/usr/bin/python3
""" displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. """

import MySQLdb
import sys


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM states
                   WHERE name LIKE '{}' """.format(sys.argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
