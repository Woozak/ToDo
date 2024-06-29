from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Tasks
from schemas import Task, TaskCreate, TaskUpdate


def get_task(db: Session, task_id: int):
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Tasks).offset(skip).limit(limit).all()


def create_task(db: Session, task: TaskCreate):
    db_task = Tasks(title=task.title, description=task.description)
    if not db_task.title:
        raise HTTPException(status_code=400, detail="The 'title' field is required and cannot be empty")
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(Tasks).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Item not found")
    db_task.title = task.title
    if not db_task.title:
        raise HTTPException(status_code=400, detail="The 'title' field is required and cannot be empty")
    db_task.description = task.description
    db_task.completed = task.completed
    db.commit()
    return db_task


def delete_task(db: Session, task_id: int):
    del_task = db.query(Tasks).filter(Tasks.id == task_id).delete()
    db.commit()
    return del_task
