#!/usr/bin/python3
"""
Defines the State class and creates the Base instance.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that represents the states table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    
    engine = create_engine('mysql+mysqldb://username:password@localhost/database', pool_pre_ping=True)

    Base.metadata.create_all(engine)
