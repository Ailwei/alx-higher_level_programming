#!/usr/bin/python3
"""
Lists all State objects and their corresponding
City objects contained in the database.
This script takes three arguments: MySQL username, MySQL password, and databas.
The connection to the MySQL server is established on localhost at port 3306.
Results are sorted in ascending order by states.id and cities.id.
The output format is as follows:
    <state id>: <state name>
        <city id>: <city name>
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)I
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by(
            State.id,
            City.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
