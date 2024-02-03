from sqlalchemy.orm import Session
from models.student import Student
from schemas.student_schema import StudentCreate
from fastapi import HTTPException



def create_student(db: Session, student: StudentCreate):
    try:
        db_student = Student(name=student.name, dept_id=student.dept_id, dob=student.dob)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def get_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")
    return db_student   

def get_all_students(db: Session):
    return db.query(Student).all()



def update_student(db: Session, student_id: int, student_data: StudentCreate):
    try:
        db_student = db.query(Student).filter(Student.id == student_id).first()
        db_student.name = student_data.name
        db_student.dept_id = student_data.dept_id
        db_student.dob = student_data.dob
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


    
def delete_student(db: Session, student_id: int):
    try:
        db_student = db.query(Student).filter(Student.id == student_id).first()
        db.delete(db_student)
        db.commit()
        return {"message": f"Student with id {student_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
