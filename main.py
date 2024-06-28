from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

import crud
from schemas import Task, TaskCreate, TaskUpdate
from database import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return crud.get_task(db, task_id)


@app.get("/get/", response_model=list[Task], status_code=status.HTTP_200_OK)
def get_tasks(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)


@app.post("/create/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@app.put("/update/", response_model=Task, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db=db, task_id=task_id, task=task)


@app.get("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task_id=task_id)
