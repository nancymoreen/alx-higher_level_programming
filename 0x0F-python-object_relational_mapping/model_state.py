#!/usr/bin/python3
"""Lists states"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city in the database.

    This class defines the structure of the 'cities' table in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The ID of the state to which the city belongs.
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
