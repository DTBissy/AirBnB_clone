#!/usr/bin/python3
"""This module instantiates an object of the appropriate storage class"""
import os

# Import classes and models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

# Dictionary of classes
class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity,
}

# Conditional import and instantiation based on environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload storage
storage.reload()
