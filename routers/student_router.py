from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.student_schema import StudentCreate, StudentRead
from crud.crud_student import create_student
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
    return create_student(db=db, student=student)

# Add more routes as needed
