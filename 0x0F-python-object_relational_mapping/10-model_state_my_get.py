#!/usr/bin/python3
"""some doc doc"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    usrname, password, dbname, state = argv[1:]
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(usrname, password, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == state).first()
    if result:
        print(result.id)
    else:
        print('Not found')
