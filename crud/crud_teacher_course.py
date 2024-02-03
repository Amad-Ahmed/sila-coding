from sqlalchemy.orm import Session
from models.teacher_course import TeacherCourse
from fastapi import HTTPException


def create_teacher_course(db: Session, teacher_id: int, course_id: int):
    try:
        teacher_course = TeacherCourse(teacher_id=teacher_id, course_id=course_id)
        db.add(teacher_course)
        db.commit()
        db.refresh(teacher_course)
        return teacher_course
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def get_teacher_course(db: Session, teacher_id: int, course_id: int):
    try:
        return db.query(TeacherCourse).filter(TeacherCourse.teacher_id == teacher_id, TeacherCourse.course_id == course_id).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_teacher_courses(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(TeacherCourse).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_teacher_courses_by_teacher(db: Session, teacher_id: int):
    try:
        return db.query(TeacherCourse).filter(TeacherCourse.teacher_id == teacher_id).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_teacher_course(db: Session, teacher_course_id: int):
    try:
        teacher_course = db.query(TeacherCourse).filter(TeacherCourse.id == teacher_course_id).first()
        db.delete(teacher_course)
        db.commit()
        return {"message": f"Teacher-Course relationship with id {teacher_course_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete_teacher_course_by_teacher_course(db: Session, teacher_id: int, course_id: int):
    try:
        teacher_course = db.query(TeacherCourse).filter(TeacherCourse.teacher_id == teacher_id, TeacherCourse.course_id == course_id).first()
        db.delete(teacher_course)
        db.commit()
        return {"message": f"Teacher-Course relationship successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))