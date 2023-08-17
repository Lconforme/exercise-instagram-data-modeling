import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_password = Column(String(250), nullable=False)
    user = Column(ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    DOB = Column(Integer, nullable=True)
    phone_number = Column(Integer, nullable=True)
    gender = Column(String(250), nullable=False)
    follower = Column(ForeignKey('Follower.id'))
    post = Column(ForeignKey('Post.id'))

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    DOB = Column(Integer, nullable=True)
    phone_number = Column(Integer, nullable=True)
    gender = Column(String(250), nullable=False) 


class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True) ## ID of the user who owns this post
    caption = Column(String(250), nullable=True) ## Photo caption
    user_id = Column(Integer, nullable=True) ##ID of the user who owns this photo
    like_numbers = Column(Integer, nullable=True) ## how many likes the photo has
    comment = Column(ForeignKey('Comment.id'))


class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(500), nullable=True)

    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e