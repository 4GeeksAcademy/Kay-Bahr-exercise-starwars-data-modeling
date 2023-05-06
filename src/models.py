import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
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
    favorites = relationship('Favorites', back_populates='user')

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
    user_id = Column(Integer, ForeignKey('User.user_id'))
    user = relationship('User', uselist=False, back_populates='login')

    def serialize(login):
        return {
            "username": login.username,
            "password": login.password,
            "id": login.user_id
        }

class Favorites(Base):
    __tablename__ = 'Favorites'

    list_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    user = relationship('User', back_populates='favorites')
    items = relationship('Items', secondary='favorites_items', back_populates='favorites')

    def serialize(favorites):
        return {
            "list id": favorites.list_id,
            "user id": favorites.user_id,
            "items": [item.to_dict() for item in favorites.items]
        }

favorites_items = Table('favorites_items', Base.metadata,
    Column('favorites_list_id', Integer, ForeignKey('Favorites.list_id')),
    Column('items_item_name', String(250), ForeignKey('Items.item_name'))
)

class Items(Base):
    __tablename__ = 'Items'

    item_name = Column(String(250), primary_key=True)
    item_type = Column(String(250), nullable=False)
    data = Column(String(250), nullable=False)
    favorites = relationship('Favorites', secondary='favorites_items', back_populates='items')

    def serialize(items):
        return {
            "name": items.item_name,
            "type": items.item_type,
            "data": items.data,
            "favorites": [favorite.to_dict() for favorite in items.favorites]
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')