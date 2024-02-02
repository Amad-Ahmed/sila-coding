from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.department_schema import DepartmentCreate, DepartmentRead
from database import SessionLocal
import crud.crud_department as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/departments/", response_model=DepartmentRead)
def add_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)


@router.get("/departments/{department_id}", response_model=DepartmentRead)
def read_department(department_id: int, db: Session = Depends(get_db)):
    return crud.get_department(db, department_id=department_id)

@router.put("/departments/{department_id}", response_model=DepartmentRead)
def update_department(department_id: int, department: DepartmentCreate, db: Session = Depends(get_db)):
    return crud.update_department(db, department_id=department_id, department_update=department)

@router.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    return crud.delete_department(db, department_id=department_id)

