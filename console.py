#!/usr/bin/python3
"""Defines the HBNB Console Module"""
import cmd 
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Con
    """


    prompt = "(hbnb)"
    __classes = {
            "BaseModel",
            "user",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }
    def emptyline(self):
        """
        Ignore empty spaces.
        """
        pass


    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True


    def do_EOF(self, line):
        """
        EOF signal to exit the program.
        """
        print("")
        return True

    def do_create(self, line):
        """
        Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        create a new class instance with given keys/values and its id.
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            class_name = args[0]
            if class_name not in self.__classes:
                raise NameError()
            kwargs = {}
            for pair in args[1:]:
                key, value = pair.split("=", 1)
                kwargs[key] = eval(value)
            obj =eval(class_name)(**kwargs)
            storage.new(obj)
            print(obj.id)
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")


    def do_show(self, line):
        """
        Prints the string representation of an instance.
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            class_name, obj_id = args[0], args[1]
            if class_name not in self.__classes:
                raise NameError()
            obj_key = "{}.{}".format(class_name, obj_id)
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                raise KeyError()
            except (SyntaxError, IndexError):
                print("** instance id missing **")
            except NameError:
                print("** no instance found **")


    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id 
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            class_name,obj_id = args[0], args[1]
            if class_name not in self.__classes:
                raise NameError()
            obj_key = "{}.{}".fornat(class_name, obj_id)
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                raise KeyError()
        except (SyntaxError, IndexError):
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
