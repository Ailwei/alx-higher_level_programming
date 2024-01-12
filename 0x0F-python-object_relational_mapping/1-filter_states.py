#!/usr/bin/python3
"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb as db
from sys import argv

    """
    Access the database and get states from the database
    """

if __name__ == '__main__':
    

conn = db.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        password=argv[2],
        db=argv[3])

cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

row_selected = cur.fetchall()

for row in row_selected:
    print(row)
