import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from database.db_setup import Base


class Status(enum.StrEnum):
    admin = "admin"
    manager = "manager"
    employee = "employee"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(Enum(Status), default=Status.employee, nullable=True)
    # tasks = relationship("Task", back_populates="user_id")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    status = Column(Text, nullable=True)
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    # user = relationship("User", back_populates="tasks")
