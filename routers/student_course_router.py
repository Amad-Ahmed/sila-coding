# routers/student_course_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.crud_student_course as crud
from database import SessionLocal

from schemas.student_course_schema import StudentCourseCreate, StudentCourseDelete


router = APIRouter()
router.tags = ["student-course"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/student-course/", response_model=StudentCourseCreate, tags=["student-course"])
def create_student_course(student_course: StudentCourseCreate, db: Session = Depends(get_db)):
    return crud.add_student_to_course(db=db, student_id=student_course.student_id, course_id=student_course.course_id)

@router.get("/student-course/{student_id}", tags=["student-course"])
def read_student_courses(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student_courses(db, student_id=student_id)

@router.delete("/student-course/", tags=["student-course"])
def delete_student_course(student_course: StudentCourseDelete, db: Session = Depends(get_db)):
    if crud.remove_student_from_course(db=db, student_id=student_course.student_id, course_id=student_course.course_id):
        return {"message": "Student removed from course successfully"}
    raise HTTPException(status_code=404, detail="Student or course not found")
