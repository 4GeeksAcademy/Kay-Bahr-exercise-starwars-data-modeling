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

    user_id = Column(Integer, ForeignKey('user.user_id'))
    username = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)

    def serialize(login):
        return {
            "id": login.user_id,
            "username": login.username,
            "password": login.password
        }

class Favorites(Base):
    __tablename__ = 'Favorites'

    list_id = Column(Integer, primary_key=True)
    item_name = Column(String(250), ForeignKey('items.item_name'))
    user_id = Column(Integer, ForeignKey('user.user_id'))

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

    def serialize(items):
        return {
            "name": items.item_name,
            "type": items.item_type,
            "data": items.data
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
