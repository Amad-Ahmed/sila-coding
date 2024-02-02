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


# Read operation
def get_department(db: Session, department_id: int):
    return db.query(Department).filter(Department.id == department_id).first()

# Update operation
def update_department(db: Session, department_id: int, department_update: DepartmentCreate):
    db_department = db.query(Department).filter(Department.id == department_id).first()
    db_department.name = department_update.name
    db.commit()
    db.refresh(db_department)
    return db_department

# Delete operation
def delete_department(db: Session, department_id: int):
    db_department = db.query(Department).filter(Department.id == department_id).first()
    db.delete(db_department)
    db.commit()
    return {"ok": True}

