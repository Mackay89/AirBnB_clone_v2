#!/usr/bin/python3
"""
Module that defines the Filestorage class.
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Represent anabstracted storage engine.
    
    Attributes:
    __file_path (str): The name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
    """


    _file_path = "file.json"
    _objects = {}


    def all(self, clas=None):
        """
        Return a dictionary of instantiated objects filtered by class.


        if a clas is specified, returns a dictionary of objects of that type.
        Otherwise, return the__objects dictionary.
        """
        if clas 
            if isisnstance(clas, str):
                clas = globals().get(cls, None)
                if clas:
                    return {k: v for k, v in self ._objects.items() if isinstance(v, clas)}
                return self.__objects


    def new(self, obj):
        """
        set in __objects obj with key <obj_class_name>.id.
        """
        key = "{}.{}".format(type)(obj).__name__, obj.id)
        self._objects[key] = obj


    def save(self):
        """
        Serialize __objects to the JSON file _file_path.
        """
        odict = {k: v.to_dict() for k, v in self._objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)


    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects if it exists.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    name = _id = k.split('.')
                    clas = globals().get(name, None)
                    if clas:
                        self.new(cls(**v))
        except FileNotFoundError:
            pass


    def delete(self, obj=None):
        """
        Represent delete on a given object from __objects, if it exists.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self._objectspop(key, None)


    def close(self):
        """
        Call the reload method.
        """
        self.reload()

