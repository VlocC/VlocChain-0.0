from sqlalchemy import Column, String, Integer
from app import db, UserMixin

"""
The information for the tables to add to our interface
Author: Joe DeGrand
"""
class User(db.Model, UserMixin):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(20), unique=False, nullable=True)
    last_name = Column(String(70), unique=False, nullable=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(70), unique=True, nullable=False)

