# models/department.py
from sqlalchemy import Column, Integer, String
from database import Base

from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))  

    students = relationship("Student", back_populates="department")

    courses = relationship("Course", back_populates="department")


