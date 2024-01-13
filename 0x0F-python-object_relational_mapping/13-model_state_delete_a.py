#!/usr/bin/python3
"""
Deletes all State objects with a name containing the
letter 'a' from the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the database and deletes all State
    objects with a name containing 'a'.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_to_delete:
        session.delete(state)

    session.commit()
    session.close()
