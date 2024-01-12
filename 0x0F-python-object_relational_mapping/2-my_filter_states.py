#!/usr/bin/python3
"""i
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

"""
Access to the database and get the states
from the database.
"""

if __name__ == '__main__':
    con = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], password=argv[2], db=argv[3])
    cur = con.cursor()
    state_name = argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    row_selected = cur.fetchall()
    for row in row_selected:
        print(row)
