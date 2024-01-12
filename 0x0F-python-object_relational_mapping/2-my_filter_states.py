#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    try:
        """
        Access to the database and get states from the database.
        """

        # Establish a connection to the MySQL server
        con = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

        # Create a cursor object to interact with the database
        cur = con.cursor()

        # Create the SQL query using user input
        query = "
        SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])

        # Execute the query
        cur.execute(query)

        # Fetch all the rows selected by the query
        rows_selected = cur.fetchall()

        # Display the results
        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        # Close the database connection
        if con:
            con.close()
