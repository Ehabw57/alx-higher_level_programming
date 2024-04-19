#!/usr/bin/python3
"""Updates the row with id 2 to mexico using sql alchemy"""
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

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
