from sqlalchemy.orm import Session
from models.student_course import StudentCourse
from fastapi import HTTPException


def get_course_students(db: Session, course_id: int):
    try:
        return db.query(StudentCourse).filter_by(course_id=course_id).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_all_student_courses(db: Session):
    try:
        return db.query(StudentCourse).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def add_student_to_course(db: Session, student_id: int, course_id: int):
    try:
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(student_course)
        db.commit()
        db.refresh(student_course)
        return student_course
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def remove_student_from_course(db: Session, student_id: int, course_id: int):
    student_course = db.query(StudentCourse).filter_by(student_id=student_id, course_id=course_id).first()
    if not student_course:
        raise HTTPException(status_code=404, detail="Student-Course relationship not found")
    try:
        db.delete(student_course)
        db.commit()
        return {"message": "Student removed from course successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
