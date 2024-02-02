from sqlalchemy.orm import Session
from models.student import Student
from schemas.student_schema import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, dept_id=student.dept_id, dob=student.dob)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Read operation
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# Update operation
def update_student(db: Session, student_id: int, student_data: StudentCreate):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db_student.name = student_data.name
    db_student.dept_id = student_data.dept_id
    db_student.dob = student_data.dob
    db.commit()
    db.refresh(db_student)
    return db_student

# Delete operation
def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db.delete(db_student)
    db.commit()
    return {"ok": True}
