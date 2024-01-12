#!/usr/bin/python3
"""Script that lists all State objects containing the letter 'a'
   from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states_with_a(username, password, db_name):
    """List all State objects containing the letter 'a'
       from the database hbtn_0e_6_usa"""
    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create the 'states' table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing the letter 'a' and print the results
    states_with_a = (session.query(State)
                     .filter(State.name.like('%a%'))
                     .order_by(State.id)
                     .all())

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states with the letter 'a'
    list_states_with_a(username, password, db_name)
