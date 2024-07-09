#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

STO_TYP = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """Getter for cities based on the storage type"""
        if STO_TYP == "db":
            storage = models.storage
            city_objects = storage.all("City")
            filtered_cities = [city for city in city_objects.values() if city.state_id == self.id]
            return filtered_cities
        else:
            return []
