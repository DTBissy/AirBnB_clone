#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from datetime import datetime
import json
from models import amenity, city, place, review, state, user


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Gets all objects from storage, optionally filtered by class"""
        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in self.__objects.items()}
            for key, val in temp.items():
                # Convert datetime objects to strings in ISO 8601 format
                for attr, value in val.items():
                    if isinstance(value, datetime):
                        temp[key][attr] = value.isoformat()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes objects from __objects"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]


    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Calls the reload method"""
        self.reload()
    
