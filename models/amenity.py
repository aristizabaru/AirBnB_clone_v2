#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = relationship(
        "Place", backref="amenities", secondary=Place.place_amenity, viewonly=False
    )
