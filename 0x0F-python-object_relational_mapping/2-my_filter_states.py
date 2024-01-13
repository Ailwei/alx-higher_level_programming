#!/usr/bin/python3
"""
This script retrieves and displays all values in the 'states'
where the 'name' matches the provided argument
from the database 'hbtn_0e_0_usa'.

Usage:
    - Ensure that you have the MySQLdb library installed:
      pip install mysqlclient
    - Provide the necessary arguments
Example:
    ./script_name.py <username> <password> <database> <state_name>

The script connects to the specified MySQL database
running on localhost at port 3306.
It fetches and prints the rows from the 'states'
table where the 'name' matches the provided argument.
Results are sorted in ascending order by 'states.id'.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
