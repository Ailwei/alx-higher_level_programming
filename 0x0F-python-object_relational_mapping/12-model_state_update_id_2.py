#!/usr/bin/python3
"""
Changes the name of a State object in the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accesses the database, changes the
    name of the State with id=2 to 'New Mexico'.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_change = session.query(State).filter_by(id=2).first()
    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()

    session.close()
