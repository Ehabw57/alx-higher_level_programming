#!/usr/bin/python3
"""Adds a new row to the db using sqlalchemy"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    usrname, password, dbname = argv[1:]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(usrname, password, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    louis = State(name='Louisiana')
    session.add(louis)
    louis = session.query(State).filter(State.name == louis.name).first()
    print(louis.id)
