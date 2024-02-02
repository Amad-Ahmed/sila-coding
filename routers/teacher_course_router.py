from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.teacher_course_schema import TeacherCourseCreate, TeacherCourseRead
import crud.crud_teacher_course as crud
from database import SessionLocal

router = APIRouter()
router.tags = ["teacher-courses"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/teacher-courses/", response_model=TeacherCourseRead,tags=["teacher-courses"])
def add_teacher_course(teacher_course: TeacherCourseCreate, db: Session = Depends(get_db)):
    return crud.create_teacher_course(db=db, teacher_id=teacher_course.teacher_id, course_id=teacher_course.course_id)

@router.get("/teacher-courses/{teacher_course_id}", response_model=TeacherCourseRead,tags=["teacher-courses"])
def read_teacher_course(teacher_course_id: int, db: Session = Depends(get_db)):
    db_teacher_course = crud.get_teacher_course(db, teacher_course_id=teacher_course_id)
    if db_teacher_course is None:
        raise HTTPException(status_code=404, detail="TeacherCourse not found")
    return db_teacher_course

# get all teacher courses
@router.get("/teacher-courses/", response_model=list[TeacherCourseRead],tags=["teacher-courses"])
def read_all_teacher_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teacher_courses(db, skip=skip, limit=limit)

# get all courses for a teacher
@router.get("/teacher-courses/teacher/{teacher_id}", response_model=list[TeacherCourseRead],tags=["teacher-courses"])
def read_teacher_courses(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_teacher_courses_by_teacher(db, teacher_id=teacher_id)



@router.delete("/teacher-courses/{teacher_course_id}", tags=["teacher-courses"])
def remove_teacher_course(teacher_course_id: int, db: Session = Depends(get_db)):
    result = crud.delete_teacher_course(db, teacher_course_id=teacher_course_id)
    if not result.get("ok"):
        raise HTTPException(status_code=404, detail="TeacherCourse not found")
    return result

# remove using teacher and course id
@router.delete("/teacher-courses/", tags=["teacher-courses"])
def remove_teacher_course_by_teacher_course(teacher_course: TeacherCourseCreate, db: Session = Depends(get_db)):
    result = crud.delete_teacher_course_by_teacher_course(db, teacher_id=teacher_course.teacher_id, course_id=teacher_course.course_id)
    if not result.get("ok"):
        raise HTTPException(status_code=404, detail="TeacherCourse not found")
    return result
