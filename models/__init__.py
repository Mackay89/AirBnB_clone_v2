#!/usr/bin/python3
"""
Instantiates a storage object based on the enviroment variable.
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage_type = getenv("HBNB_TYPE_STORAGE")


if STORAGE_TYPE == "db":
    STORAGE = dBStorage()
else:
    storage = FileStorage()


storage.reload()

