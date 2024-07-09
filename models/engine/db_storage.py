#!/usr/bin/python3
"""DBStorage module for HBNB project"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
from models.engine.file_storage import FileStorage
# Import other models as necessary

class DBStorage:
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None
    __file_storage = FileStorage()


    def __init__(self):
        """Initialize the storage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects or specific class objects from the current database session"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            for model in [City, State]:  # Add other models as needed
                objs = self.__session.query(model).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        from models.user import User  # Ensure all models are imported
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session() 
        
    @property
    def file_storage(self):
        """Get the file storage instance"""
        return self.__file_storage

    def close(self):
        """Close the current database session"""
        self.__session.close()
