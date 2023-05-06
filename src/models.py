import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    name_last = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def serialize(user):
        return {
            "id": user.user_id,
            "name": user.name,
            "last name": user.name_last,
            "email": user.email
        }
    
class Login(Base):
    __tablename__ = 'Login'

    username = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)

    def serialize(login):
        return {
            "username": login.username,
            "password": login.password,
            "id": login.user_id
        }

class Favorites(Base):
    __tablename__ = 'Favorites'

    list_id = Column(Integer, primary_key=True)
    item_name = Column(String(250), ForeignKey('items.item_name'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)

    def serialize(favorites):
        return {
            "list id": favorites.list_id,
            "item name": favorites.item_name,
            "user id": favorites.user_id
        }

class Items(Base):
    __tablename__ = 'Items'

    item_name = Column(String(250), primary_key=True)
    item_type = Column(String(250), nullable=False)
    data = Column(String(250), nullable=False)
    favorites = relationship(Favorites)

    def serialize(items):
        return {
            "name": items.item_name,
            "type": items.item_type,
            "data": items.data
        }

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
