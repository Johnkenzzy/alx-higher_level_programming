#!/usr/bin/python3
"""
Changes State object name of id `2` to “New Mexico”
in the database hbtn_0e_6_usa
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
    state = session.query(State).filter_by(id=2).one()
    state.name = 'New Mexico'
    session.commit()
    session.close()
