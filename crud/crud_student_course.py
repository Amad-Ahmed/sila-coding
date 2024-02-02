# crud/crud_student_course.py
from sqlalchemy.orm import Session
from models.student_course import StudentCourse

def add_student_to_course(db: Session, student_id: int, course_id: int):
    student_course = StudentCourse(student_id=student_id, course_id=course_id)
    db.add(student_course)
    db.commit()
    db.refresh(student_course)
    return student_course

def remove_student_from_course(db: Session, student_id: int, course_id: int):
    student_course = db.query(StudentCourse).filter_by(student_id=student_id, course_id=course_id).first()
    if student_course:
        db.delete(student_course)
        db.commit()
        return True
    return False
