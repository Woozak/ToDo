from sqlalchemy.orm import Session
from models import Tasks
from schemas import Task, TaskCreate, TaskUpdate


def get_task(db: Session, task_id: int):
    return db.query(Tasks).filter(Tasks.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Tasks).offset(skip).limit(limit).all()


def create_task(db: Session, task: TaskCreate):
    db_task = Tasks(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(Tasks).get(task_id)
    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db.commit()
    return db_task


def delete_task(db: Session, task_id: int):
    del_task = db.query(Tasks).filter(Tasks.id == task_id).delete()
    db.commit()
    return del_task
