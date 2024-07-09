#!/usr/bin/python3
"""This module defines a class User"""
import hashlib
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
STO_TYP = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """ This is a class that is very frusting to make 
    but hey that part of the journey.
    Any ways there is is forming relations ships with others
    """
    if STO_TYP == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''