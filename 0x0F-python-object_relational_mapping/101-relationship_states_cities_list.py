#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_x_cities = session.query(State, City).filter(
            State.id == City.state_id).order_by(
                    State.id, City.id).all()
    curr_state_id = None
    for state, city in states_x_cities:
        if state.id != curr_state_id:
            print(f"{state.id}: {state.name}")
            curr_state_id = state.id
        print(f"\t{city.id}: {city.name}")
