#!/usr/bin/python3
""" The state class"""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import string
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state for a location in the database.
    Attributes:
    name (str): The name of the state.
    cities (relationship): The relationship with City objects.
    """
    __tablename__ = "states"
    name = Column(string(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")
    
    @property
    def cities(self):
        """
        Getter method for cities associated with this state.
        """
        cities_lst = []
        for city in models.storage.all().values():
            if isinstance(city, City) and city.state_id == self.id:
                cities_lst.append(city)
        return cities_lst
