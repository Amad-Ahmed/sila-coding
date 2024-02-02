from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher_schema import TeacherCreate

def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(name=teacher.name, dept_id=teacher.dept_id)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, teacher_data: TeacherCreate):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher:
        db_teacher.name = teacher_data.name
        db_teacher.dept_id = teacher_data.dept_id
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return {"ok": True}
