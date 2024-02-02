from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    credits = Column(Integer, nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))

    # Relationship to the Department model (if you have a Department model defined)
    department = relationship("Department", back_populates="courses")

    # Relationship to the StudentCourse model (if you have a StudentCourse model defined)
    students = relationship("StudentCourse", back_populates="course")

