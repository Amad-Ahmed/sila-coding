from sqlalchemy.orm import Session
from models.course import Course
from schemas.course_schema import CourseCreate
from fastapi import HTTPException

def get_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} not found")
    return db_course

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Course).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

def create_course(db: Session, course: CourseCreate):
    db_course = Course(**course.dict())
    db.add(db_course)
    try:
        db.commit()
        db.refresh(db_course)
        return db_course
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not create course")


def update_course(db: Session, course_id: int, course_data: CourseCreate):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} not found")
    for var, value in vars(course_data).items():
        setattr(db_course, var, value) if value else None
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail=f"Course with id {course_id} not found")
    db.delete(db_course)
    db.commit()
    return {"message": f"Course with id {course_id} successfully deleted"}
