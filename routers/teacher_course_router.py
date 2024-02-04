from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from schemas.teacher_course_schema import TeacherCourseCreate, TeacherCourseRead
import crud.crud_teacher_course as crud
from database import SessionLocal
import io
import csv



router = APIRouter()
router.tags = ["teacher-courses"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoint to create a new teacher-course
@router.post("/teacher-courses/", response_model=TeacherCourseRead, tags=["teacher-courses"])
def add_teacher_course(teacher_course: TeacherCourseCreate, db: Session = Depends(get_db)):
    return crud.create_teacher_course(db=db, teacher_id=teacher_course.teacher_id, course_id=teacher_course.course_id)
    

# endpoint to upload a CSV file
@router.post('/teacher-courses/upload-csv/', tags=["teacher-courses"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the rest of your processing logic is correct
        teacherCourse = TeacherCourseCreate(**row)
        crud.create_teacher_course(db=db, teacher_id=teacherCourse.teacher_id, course_id=teacherCourse.course_id)
    return {"message": "CSV has been processed"}


# endpoint to read teacher-course by its course id
@router.get("/teacher-courses/{course_id}", response_model=TeacherCourseRead,tags=["teacher-courses"])
def read_teacher_course(course_id: int, db: Session = Depends(get_db)):
    return crud.get_teachers_by_course(db, course_id=course_id)
    

# endpoint to read all teacher-courses
@router.get("/teacher-courses/", response_model=list[TeacherCourseRead],tags=["teacher-courses"])
def read_all_teacher_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teacher_courses(db, skip=skip, limit=limit)


# endpoint to read teacher-course by its teacher id
@router.get("/teacher-courses/teacher/{teacher_id}", response_model=list[TeacherCourseRead],tags=["teacher-courses"])
def read_teacher_courses(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_teacher_courses_by_teacher(db, teacher_id=teacher_id)


# endpoint to remove teacher-course by its teacher-course-id
@router.delete("/teacher-courses/{teacher_course_id}", tags=["teacher-courses"])
def remove_teacher_course(teacher_course_id: int, db: Session = Depends(get_db)):
    return crud.delete_teacher_course(db, teacher_course_id=teacher_course_id)
    

# endpoint to remove teacher-course by its teacher id and course id
@router.delete("/teacher-courses/", tags=["teacher-courses"])
def remove_teacher_course_by_teacher_course(teacher_course: TeacherCourseCreate, db: Session = Depends(get_db)):
    return crud.delete_teacher_course_by_teacher_course(db, teacher_id=teacher_course.teacher_id, course_id=teacher_course.course_id)
   
