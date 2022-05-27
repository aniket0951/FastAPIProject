# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def index():
#     return "idexing"

from operator import imod
from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
import api

app = FastAPI()

# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/user", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/student", response_model=schemas.StudentInfo)
def create_student(student:schemas.StudentCreate, db: Session = Depends(get_db)):

    db_user = crud.get_students(db, name=student.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Student already registered")
    return crud.create_student(db=db, student=student)    

@app.get("/studentdata", response_model=schemas.StudentInfo)
def getStudents(db: Session = Depends(get_db)):
    return crud.get_students(db, name="string")