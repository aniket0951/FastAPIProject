from ast import Str
from sqlalchemy import Column, Integer, String
from database import Base


#  user tables
class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String, unique=True)

# for the student table
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    roll = Column(Integer)
    city = Column(String) 