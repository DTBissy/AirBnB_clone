#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from sqlalchemy import Table
from models.amenity import Amenity

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                              Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                              )

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """ Getter attribute amenities that returns the list of Amenity instances """
            amenities_list = []
            from models import storage
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list
