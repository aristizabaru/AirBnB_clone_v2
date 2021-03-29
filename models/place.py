#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy import Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    # Table attributes and columns
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    metadata = Base.metadata
    # Creating a new table for the many to many relationship
    place_amenity = Table('place_amenity', metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
    )

    #Relationships bewteen tables
    reviews = relationship("Review", backref="place")
    amenities = relationship(
        "Amenity", back_populates="places", secondary=place_amenity, viewonly=False
    )

    @property
    def reviews(self):
        from models import storage
        """getter attribute cities that returns the
        list of City instances with state_id"""
        place_reviews= list()
        all_reviews = storage.all("Review")
        for key,value in all_reviews.items():
            if value.place_id == self.id:
                place_reviews.append(value)
        return place_reviews

    @property
    def amenities(self):
        from models import storage
        """getter attribute cities that returns the
        list of City instances with state_id"""
        place_amenities= list()
        all_amenities = storage.all("Amenity")
        for key,value in all_amenities.items():
            if value.id in type(self).amenity_ids:
                place_amenities.append(value)
        return place_amenities

    @amenities.setter
    def amenities(self, obj):
        from models import storage
        """getter attribute cities that returns the
        list of City instances with state_id"""
        if obj.__class__.__name__ == "Amenity":
            self.amenities.append(obj)
