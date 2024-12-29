#!/usr/bin/python3
"""
Defines the State class that inherits from the
Base class object to define mapped class
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State Class

    This class represents the 'states' table in the database and maps its
    columns to the class attributes using SQLAlchemy's
    Object-Relational Mapping (ORM).

    Attributes:
    ----------
    __tablename__ : str
        The name of the table in the database associated with this class.

    id : int
        Unique identifier for each state. It is auto-incremented primary key.
        - Column type: Integer
        - Constraints: Unique, Non-nullable, Primary key

    name : str
        The name of the state.
        - Column type: String (max length: 128 characters)
        - Constraints: Non-nullable

    cities (relationship) :
        The list of City objects associated with the state.
    """
    __tablename__ = 'states'
    id = Column(
            Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

# City.state = relationship("State", order_by=State.id, back_populates="state")
