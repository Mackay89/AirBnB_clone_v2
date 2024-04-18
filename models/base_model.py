#!/usr/bin/python3
"""
Module that defines the BaseModel class.
"""
import models
from uuid import uuid4
from datatime import datetime 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """
    Defines the BaseModel class.


    Attributes:
    id (sqlalchemy String): The BaseModel id.
    created_at (sqlalchemy DateTime): The datetime at creation.
    updated_at (sqlalchemy DateTime): The datatime of last update.
    """


    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DataTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


    def __init__(self, *args, **Kwargs):
        """
        Initialize a new BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    value = datetime.strptime(value, "%Y-%m-%dt%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())

            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.update_at = datetime.now()
        else:
            selft.id = str(uuid4())
            selft.created_at = self.updated_at = datetime.now()


    def save(self):
        """
        Update updated_at with the current datime and save to storage.
        """
        self.update_at = datetime.now()
        models.storage.new(self)
        models.storage.save()


    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        """
        my_dict = self.__dict__.copy()
        my_dict.pop("_sa_instance_state", None)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["update_at"] = self.update_at.isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict


    def delete(self):
        """
        Delete the currect instance from storage.
        """
        models.storage.delete(self)


    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items()
                if k != "_sa_instance_state")
        return '[{}] ({}) {{{}}}".format(type(self).__name__, self.id, attrs)
