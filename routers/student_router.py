from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.student_schema import StudentCreate, StudentRead
import crud.crud_student as crud
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=StudentRead)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@router.get("/students/{student_id}", response_model=StudentRead)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id=student_id)

@router.put("/students/{student_id}", response_model=StudentRead)
def update_student_endpoint(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id=student_id, student_data=student)

@router.delete("/students/{student_id}")
def delete_student_endpoint(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id=student_id)
