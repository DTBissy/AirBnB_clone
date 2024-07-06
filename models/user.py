#!/usr/bin/python3
""" THis module defines a class User"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class definition."""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # places = relationship("Place", backref="owner_user", cascade="all, delete-orphan")
