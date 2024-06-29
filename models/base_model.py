#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    __tablename__ = 'BaseModel'

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.strptime(kwargs.get('created_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs.get('updated_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = datetime.strptime(kwargs.get('created_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs.get('updated_at', datetime.utcnow().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        from models import storage
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})

        # Remove the _sa_instance_state key if it exists
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        from models import storage
        """Delete the current instance from the storage."""
        storage.delete(self)
