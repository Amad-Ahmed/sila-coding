from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher_schema import TeacherCreate
from fastapi import HTTPException


def create_teacher(db: Session, teacher: TeacherCreate):
    try:
        db_teacher = Teacher(name=teacher.name, dept_id=teacher.dept_id)
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

def get_teacher(db: Session, teacher_id: int):
    try:
        return db.query(Teacher).filter(Teacher.id == teacher_id).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Teacher).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_teacher(db: Session, teacher_id: int, teacher_data: TeacherCreate):
    try:
        db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        db_teacher.name = teacher_data.name
        db_teacher.dept_id = teacher_data.dept_id
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete_teacher(db: Session, teacher_id: int):
    try:
        db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        db.delete(db_teacher)
        db.commit()
        return {"message": f"Teacher with id {teacher_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
