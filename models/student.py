from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))
    dob = Column(Date, nullable=False)

    # Relationship to the Department model (if you have a Department model defined)
    department = relationship("Department", back_populates="students")
