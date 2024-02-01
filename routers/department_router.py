from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.department_schema import DepartmentCreate, DepartmentRead
from crud.crud_department import create_department
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/departments/", response_model=DepartmentRead)
def add_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return create_department(db=db, department=department)
