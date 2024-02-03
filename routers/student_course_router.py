# routers/student_course_router.py
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import crud.crud_student_course as crud
from database import SessionLocal
from schemas.student_course_schema import StudentCourseCreate, StudentCourseDelete
import io
import csv

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


@router.post('/student-course/upload-csv/', tags=["student-course"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the rest of your processing logic is correct
        studentCourse = StudentCourseCreate(**row)
        crud.add_student_to_course(db=db, student_id=studentCourse.student_id, course_id=studentCourse.course_id)
    return {"message": "CSV has been processed"}


@router.get("/student-course/{student_id}", tags=["student-course"])
def read_student_courses(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student_courses(db, student_id=student_id)

@router.delete("/student-course/", tags=["student-course"])
def delete_student_course(student_course: StudentCourseDelete, db: Session = Depends(get_db)):
    if crud.remove_student_from_course(db=db, student_id=student_course.student_id, course_id=student_course.course_id):
        return {"message": "Student removed from course successfully"}
    raise HTTPException(status_code=404, detail="Student or course not found")
