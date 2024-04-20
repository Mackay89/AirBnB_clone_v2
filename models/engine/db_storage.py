#!/usr/bin/python3
"""
Module that defines the DBStorage engine.
"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """
    Represents a database storage engine.


    Attributes:
    __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
    __session (sqlalchemy.Session): The working SQLAlchemy session.
    """


    __engine = None
    __session = None
    __classes = [State, City, User, Place, Review, Amenity]


    def __init__(self)
    """
    Initialize a new DBStorage instance.
    """
    try:
        self__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format
        (getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
        pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    except OperationalError as e:
        print("Error connecting to  database:", e)


    def all(self, clas=None):
        """
        Query all objects of the given class.

        Args:
        clas (class): The class to query.


        Returns:
        dict: A dictionary of queried objects.
        """
        objects = []
        try:
            if clas:
                query = self.__session.query(clas).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
            else:
                for clas in self.__classes:
                    query = self.__session.query(clas).all()
                    for obj in query:
                        key = "{}.{}".format(type()obj).__name__, obj.id)
                        objects[key] = obj
        except AttributeError:
            print("Session not initialized. Call reload() first.")
        return objects


    def new(self, obj):
        """
        Add obj to the current databse session.
        """
        try:
            self.__session.commit()
        except AttributeError:
            print("Session not initialized. Call reload() first.")


    def delete(self, obj=None):
        """
        Represent the delete obj from the current database session.
        """
        if obj:
            try:
                self.__session.delete(obj)
            except AttributeError:
                print("Session not initialized. Call reload() first."


    def reload(self):
        """
        Create all tables in the database and initialize a new session.
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()


    def close(self):
        """
        close the working SQLAlchemy session and dispose of the engine.
        """
        try:
            self.__session.close()
            self.__engine.dispose()
        except AttributeError:
            print("Session not initialize. Call reload() first.")





