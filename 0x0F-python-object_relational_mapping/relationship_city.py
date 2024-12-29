#!/usr/bin/python3
"""
Contains the class definition of City
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Represents a city in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The ID of the state to which the city belongs.
    """
    __tablename__ = 'cities'
    id = Column(
            Integer, unique=True, autoincrement=True,
            nullable=False, primary_key=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
