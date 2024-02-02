from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class TeacherCourse(Base):
    __tablename__ = 'teacher_courses'
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    teacher = relationship("Teacher", back_populates="courses")
    course = relationship("Course", back_populates="teachers")