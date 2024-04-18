#!/usr/bin/python3
"""List the first row in the db hbtn_0e_6_usa using sql alchemy"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

usrname, passwod, dbname = argv[1:]
engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                       .format(usrname, passwod, dbname))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

first = session.query(State).first()
if first:
    print('{}: {}'.format(first.id, first.name))
else:
    print('Nothing')
