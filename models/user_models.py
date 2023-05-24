import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database.db_setup import Base


class Profile(enum.StrEnum):
    admin = "admin"
    manager = "manager"
    employee = "employee"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile = Column(Enum(Profile), default=Profile.employee, nullable=True)
    tasks = relationship("Task", back_populates="user")
