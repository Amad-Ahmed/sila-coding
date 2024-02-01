from sqlalchemy.orm import Session
from models.department import Department
from schemas.department_schema import DepartmentCreate

def create_department(db: Session, department: DepartmentCreate):
    print("INSIDE CRUD")
    db_department = Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department
