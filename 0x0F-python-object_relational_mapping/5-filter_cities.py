#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get cities of the specified state.
    """
    try:
        # Check if the correct number of arguments is provided
        if len(argv) != 5:
            print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
            exit(1)

        # Get MySQL credentials and state name from command line arguments
        username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

        # Connect to MySQL server
        con = MySQLdb.connect(
            host="localhost", user=username, port=3306, passwd=password, db=database)

        cur = con.cursor()

        # Use execute() to fetch cities of the specified state
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cur.execute(query, (state_name,))
        rows_selected = cur.fetchall()

        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)

    finally:
        if 'con' in locals() or 'con' in globals():
            cur.close()
            con.close()
