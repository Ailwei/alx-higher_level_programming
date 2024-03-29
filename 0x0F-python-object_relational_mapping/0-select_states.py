#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

        cur = conn.cursor()

        cur.execute("SELECT * FROM states")

        rows_selected = cur.fetchall()

        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)

    finally:
        if conn:
            cur.close()
            conn.close()
