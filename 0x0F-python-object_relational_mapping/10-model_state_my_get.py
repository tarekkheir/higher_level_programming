#!/usr/bin/python3
"""
script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":

    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State)
    state1 = state.filter(State.name == state_name)
    state2 = state1.order_by(State.id).first()

    if state2:
        print("{}".format(state2.id))

    else:
        print("Not found")

    session.close()
