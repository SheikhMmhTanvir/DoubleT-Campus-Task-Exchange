from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
import datetime

#One to Many

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False, unique=True)
    tasks=relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String, nullable=False)
    description=Column(String)
    budget=Column(Integer)
    status=Column(String, default="Open")
    user_id=Column(Integer, ForeignKey("users.id"))
    owner=relationship("User", back_populates="tasks")
