#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the MySQL server
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the new State object to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)
