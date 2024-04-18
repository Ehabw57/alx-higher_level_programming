#!/usr/bin/python3
"""_______-"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    usrname, passwod, dbname = argv[1:]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                           format(usrname, passwod, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)

    for row in result:
        print('{}: {}'.format(row.id, row.name))
