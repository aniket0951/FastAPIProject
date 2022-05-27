from typing import List
from unicodedata import name
from pydantic import BaseModel


class UserInfoBase(BaseModel):
    username: str
    fullname: str


class UserCreate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True


# for the student class
class StudentInfoBase(BaseModel):
    name: str
    roll: int
    # city: str

class StudentCreate(StudentInfoBase):
    city: str

class StudentInfo(StudentInfoBase):
    id: int

    class Config:
        orm_mode= True