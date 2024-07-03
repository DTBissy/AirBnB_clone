#!/usr/bin/python3
"""This module defines a class City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """This class represents a city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # state = relationship('State', backref='cities')