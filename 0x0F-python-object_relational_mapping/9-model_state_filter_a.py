#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":

    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()
