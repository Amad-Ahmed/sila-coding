from sqlalchemy.orm import Session
from models.department import Department
from schemas.department_schema import DepartmentCreate
from fastapi import HTTPException


def create_department(db: Session, department: DepartmentCreate):
    try:
        db_department = Department(name=department.name)
        db.add(db_department)
        db.commit()
        db.refresh(db_department)
        return db_department
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")



def get_department(db: Session, department_id: int):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


def update_department(db: Session, department_id: int, department_update: DepartmentCreate):
    db_department = db.query(Department).filter(Department.id == department_id).first()
    if not db_department:
        raise HTTPException(status_code=404, detail="Department not found")
    db_department.name = department_update.name
    db.commit()
    db.refresh(db_department)
    return db_department



def delete_department(db: Session, department_id: int):
    db_department = db.query(Department).filter(Department.id == department_id).first()
    if not db_department:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(db_department)
    db.commit()
    return {"ok": True, "message": f"Department with id {department_id} successfully deleted"}

