
from django.http import HttpResponse, JsonResponse
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

import models, schemas


def get_user_by_username(db: Session, username: str):
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserInfo(username=user.username, password=fake_hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# for students

def get_students(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name == name).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_user = models.Student(name=student.name, roll=student.roll, city=student.city)
    db.add(db_user)
    return JsonResponse("student added successfully")
    db.commit()
    db.refresh(db_user)
    return db_user
    return HttpResponse(status_code=200, details='student created successfully')