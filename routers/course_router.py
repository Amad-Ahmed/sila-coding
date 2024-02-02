from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.course_schema import CourseCreate, CourseRead
import crud.crud_course as crud
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/courses/", response_model=CourseRead)
def create(course: CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)

@router.get("/courses/{course_id}", response_model=CourseRead)
def read(course_id: int, db: Session = Depends(get_db)):
    return crud.get_course(db=db, course_id=course_id)

@router.get("/courses/", response_model=list[CourseRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_courses(db=db, skip=skip, limit=limit)

@router.put("/courses/{course_id}", response_model=CourseRead)
def update(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    return crud.update_course(db=db, course_id=course_id, course_data=course)

@router.delete("/courses/{course_id}")
def delete(course_id: int, db: Session = Depends(get_db)):
    return crud.delete_course(db=db, course_id=course_id)
