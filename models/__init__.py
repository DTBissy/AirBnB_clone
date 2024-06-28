#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

#!/usr/bin/python3

"""initializes FileStorage class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class_dict = {
    "BaseModel" : BaseModel,
    "User" : User,
    "City" : City,
    "State" : State,
    "Place" : Place,
    "Review" : Review,
    "Amenity" : Amenity,
}

storage = FileStorage()
storage.reload()
