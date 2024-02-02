from sqlalchemy.orm import Session
from models.student import Student
from schemas.student_schema import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, dept_id=student.dept_id, dob=student.dob)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Add more CRUD operations as needed
