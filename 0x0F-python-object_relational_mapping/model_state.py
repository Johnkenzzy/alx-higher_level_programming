#!/usr/bin/python3
"""
Defines the State class that inherits from the
Base class object to define mapped class
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(
            Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True
            )
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    State()
