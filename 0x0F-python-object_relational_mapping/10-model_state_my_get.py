#!/usr/bin/python3
"""Script that prints the State object with the name passed as an argument
   from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_state_by_name(username, password, db_name, state_name):
    """Print the State object with the given
    name from the database hbtn_0e_6_usa
    """
    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create the 'states' table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state by name and print the result
    state = (session.query(State)
             .filter(State.name == state_name)
             .first())

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username,
    password,
    db_name,
    state_name = sys.argv[1],
    sys.argv[2],
    sys.argv[3],
    sys.argv[4]

    # Call the function to print the state by name
    print_state_by_name(username, password, db_name, state_name)
