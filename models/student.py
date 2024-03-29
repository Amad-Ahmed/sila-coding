from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,BigInteger
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))
    dob = Column(DateTime, nullable=False)

    # Relationship to the Department model (if you have a Department model defined)
    department = relationship("Department", back_populates="students")

    # Relationship to the StudentCourse model (if you have a StudentCourse model defined)
    courses = relationship("StudentCourse", back_populates="student")
