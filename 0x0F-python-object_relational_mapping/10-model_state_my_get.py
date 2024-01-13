#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.

Usage:
    - Ensure that you have the required SQLAlchemy
    and MySQL libraries installed:
      pip install sqlalchemy mysqlclient
    - Provide the necessary arguments
Example:
    ./script_name.py <username> <password> <database> <state_name>

The script connects to the specified MySQL database
running on localhost at port 3306.
It retrieves and prints information about
the first State object with the specified name
from the 'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
