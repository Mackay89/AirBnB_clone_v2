#!/usr/bin/python3
"""
Module that defines the User class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Colum, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Represents a user for a MySQL database.
    Inherits from SQLAlchemy Base and link to the MySQL table users.
    Attributes:
    __tablename__ (str): The name of the MySQL table to store users.
    email: (sqlalchemy String): The user's email address.
    password (sqlalchemy String): The user's password.
    first_name (sqlalchemy String): The user's first name.
    last_name (sqlalchemy String): The user's last name.
    places (sqlalchemy relationship): The User-Place relationship.
    reviews (sqlalchemy relationship): The User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    place = relationship("Place", backref="user", cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
