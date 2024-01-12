#!/usr/bin/python3
"""
Write a script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, while preventing SQL injection.
"""

import MySQLdb
from sys import argv

def safe_filter_states(username, password, database, state_name):
    """
    Connect to the database and retrieve states
    where the name matches the provided argument.
    """
    try:
        # Connect to MySQL server
        con = MySQLdb.connect(
            host="localhost", user=username, port=3306, passwd=password, db=database)

        cur = con.cursor()

        # Use parameterized query to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        rows_selected = cur.fetchall()

        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)

    finally:
        if con:
            cur.close()
            con.close()

if __name__ == '__main__':
    """
    Main function to parse command line arguments
    and call the safe_filter_states function.
    """
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]
    safe_filter_states(username, password, database, state_name)
