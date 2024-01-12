#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get cities from the database.
    """
    try:
        # Check if the correct number of arguments is provided
        if len(argv) != 4:
            print("Usage: {} <username> <password> <database>".format(argv[0]))
            exit(1)

        # Get MySQL credentials from command line arguments
        username, password, database = argv[1], argv[2], argv[3]

        # Connect to MySQL server
        con = MySQLdb.connect(
            host="localhost", user=username, port=3306, passwd=password, db=database)

        cur = con.cursor()

        # Use execute() to fetch all cities in ascending order by cities.id
        cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
        rows_selected = cur.fetchall()

        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)

    finally:
        if 'con' in locals() or 'con' in globals():
            cur.close()
            con.close()
