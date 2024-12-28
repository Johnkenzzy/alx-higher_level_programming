#!/usr/bin/python3
"""
Lists all State objects that contain the letter `a`
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    filtered_state = session.query(State).filter(
            State.name.ilike('%{}'.format(sys.argv[4]))
            ).order_by(State.id).first()
    if filtered_state is not None:
        print(filtered_state.id)
    else:
        print("Not found")

    session.close()
