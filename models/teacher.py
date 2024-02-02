from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("Department", back_populates="teachers")

    courses = relationship("TeacherCourse", back_populates="teacher")
    