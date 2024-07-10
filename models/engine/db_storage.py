#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone
with new SQL database.
"""
from models.base_model import Base, BaseModel
import os
from models import city, place, review, state, amenity, user
from models.engine.file_storage import FileStorage


class DBStorage:
    """
    Handles long-term storage of all class instances via SQLAlchemy ORM.
    Thank you Doug.
    """
    __engine = None
    __session = None
    __file_storage = FileStorage()

    def __init__(self):
        """ Initializes the database engine. """
        from sqlalchemy import create_engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.environ['HBNB_MYSQL_USER'],
                                             os.environ['HBNB_MYSQL_PWD'],
                                             os.environ['HBNB_MYSQL_HOST'],
                                             os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ Creates database tables and initializes a new session. """
        from sqlalchemy.orm import scoped_session, sessionmaker
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def all(self, cls_name):
        """ Queries all objects of a given class from the database. """
        try:
            result = {}
            cls = eval(cls_name)
            objects = self.session.query(cls).all()
            for obj in objects:
                result[obj.id] = obj
            return result
        except Exception as e:
            print(f"Error fetching {cls_name}:")
            return {}

    def new(self, obj):
        """ Adds a new object to the session. """
        self.__session.add(obj)

    def save(self):
        """ Commits changes to the database. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the session. """
        if obj:
            self.__session.delete(obj)

    @property
    def file_storage(self):
        """ Returns the instance of FileStorage. """
        return self.__file_storage

    def close(self):
        """Handles closing the session"""
        self.__session.close()
