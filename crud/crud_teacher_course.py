from sqlalchemy.orm import Session
from models.teacher_course import TeacherCourse

def create_teacher_course(db: Session, teacher_id: int, course_id: int):
    teacher_course = TeacherCourse(teacher_id=teacher_id, course_id=course_id)
    db.add(teacher_course)
    db.commit()
    db.refresh(teacher_course)
    return teacher_course

def get_teacher_course(db: Session, teacher_course_id: int):
    return db.query(TeacherCourse).filter(TeacherCourse.id == teacher_course_id).first()

def get_teacher_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TeacherCourse).offset(skip).limit(limit).all()

def get_teacher_courses_by_teacher(db: Session, teacher_id: int):
    return db.query(TeacherCourse).filter(TeacherCourse.teacher_id == teacher_id).all()


def delete_teacher_course(db: Session, teacher_course_id: int):
    teacher_course = db.query(TeacherCourse).filter(TeacherCourse.id == teacher_course_id).first()
    if teacher_course:
        db.delete(teacher_course)
        db.commit()
    return {"ok": True}

def delete_teacher_course_by_teacher_course(db: Session, teacher_id: int, course_id: int):
    teacher_course = db.query(TeacherCourse).filter(TeacherCourse.teacher_id == teacher_id, TeacherCourse.course_id == course_id).first()
    if teacher_course:
        db.delete(teacher_course)
        db.commit()
    return {"ok": True}