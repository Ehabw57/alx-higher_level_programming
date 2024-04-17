#!/usr/bin/python3
"""A script that quring a table using sqlalchemy lib"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

args = argv[1:]
engine = create_engine('mysql://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]))
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for id, name in session.query(State.id, State.name).order_by(State.id):
        print('{}: {}'.format(id, name))
