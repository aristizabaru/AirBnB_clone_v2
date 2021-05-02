#!/usr/bin/python3
""" DB Storage for HBNB Project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
import os


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}

enviroment = {
    "HBNB_MYSQL_USER": None,
    "HBNB_MYSQL_PWD": None,
    "HBNB_MYSQL_HOST": None,
    "HBNB_MYSQL_DB": None,
    "HBNB_ENV": None
}


class DBStorage:
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Init for the DBStorage class"""
        # Load enviroment
        for key, value in enviroment.items():
            enviroment[key] = os.getenv(key)

        type(self).__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(
                enviroment["HBNB_MYSQL_USER"],
                enviroment['HBNB_MYSQL_PWD'],
                enviroment["HBNB_MYSQL_HOST"],
                enviroment['HBNB_MYSQL_DB']
            ),
            pool_pre_ping=True
        )

        if enviroment["HBNB_ENV"] == "test":
            # Drop all tables
            pass

    def all(self, cls=None):
        """query all objects depending of the class name"""
        # filter
        object_dict = dict()
        if cls:
            # result = type(self).__session.query(cls).all()
            # result = type(self).__session.query(classes[cls]).all()
            result = type(self).__session.query(eval(cls.__name__)).all()
            for item in result:
                key = item.__class__.__name__ + '.' + item.id
                object_dict[key] = item
        else:
            for key, value in classes.items():
                result = type(self).__session.query(value).all()
                for item in result:
                    object_dict[item.__class__ + '.' + item.id] = item
        return object_dict

    def new(self, obj):
        """add the object to the current database session"""
        type(self).__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        type(self).__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            type(self).__session.delete(obj)

    def close(self):
        """Close de session"""
        self.__session.remove()

    def reload(self):
        """create the current database session"""

        # Creates a shema -> create the table in memory
        Base.metadata.create_all(type(self).__engine)

        # Creates a session
        session_factory = sessionmaker(
            bind=type(self).__engine, expire_on_commit=False)
        # Session = scoped_session(session_factory)
        # type(self).__session = Session()
        type(self).__session = scoped_session(session_factory)
