#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    reslut = session.query(City, State).join(State).order_by(City.id)

    for city, state in reslut.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
