from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(50))
    description: str = Column(String(120), nullable=True)
    completed: bool = Column(Boolean, default=False)
