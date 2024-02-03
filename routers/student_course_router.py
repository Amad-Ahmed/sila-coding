# routers/student_course_router.py
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
import crud.crud_student_course as crud
from database import SessionLocal
from schemas.student_course_schema import StudentCourseCreate, StudentCourseDelete
from schemas.student_schema import StudentCreate
from schemas.course_schema import CourseCreate
import io
import csv
from models import Student, Course, StudentCourse
from datetime import datetime


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



def get_or_create(session,model,**kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
    
def extract_student_data(row):
    dob_datetime=datetime.fromisoformat(row["dob"].rstrip("Z"))
    row["dob"]=dob_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return {
        "name":row["name"],
        "dept_id":row["dept_id"],
        "dob":row["dob"],
    }

def extract_course_data(row):
    return {
        "title":row["title"],
        "description":row["description"],
        "credits":row["credits"],
        "dept_id":row["dept_id"]
    }


@router.post('/student-course/complete-upload-csv/', tags=["student-course"])
async def complete_upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        contents = contents.decode("utf-8-sig")
        file = io.StringIO(contents)
        reader = csv.DictReader(file)
        for row in reader:
            student = get_or_create(db,Student,**extract_student_data(row))
            course = get_or_create(db,Course,**extract_course_data(row))
            student_course = StudentCourse(student_id=student.id,course_id=course.id)
            db.add(student_course)
            db.commit()
        return {"message": "CSV has been processed"}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@router.post('/student-course/upload-csv/', tags=["student-course"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        studentCourse = StudentCourseCreate(**row)
        crud.add_student_to_course(db=db, student_id=studentCourse.student_id, course_id=studentCourse.course_id)
    return {"message": "CSV has been processed"}


@router.get("/student-course/{student_id}", tags=["student-course"])
def read_student_courses(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student_courses(db, student_id=student_id)

@router.get("/student-course/{course_id}", tags=["student-course"])
def read_course_students(course_id: int, db: Session = Depends(get_db)):
    return crud.get_course_students(db, course_id=course_id)





@router.delete("/student-course/", tags=["student-course"])
def delete_student_course(student_course: StudentCourseDelete, db: Session = Depends(get_db)):
    return crud.remove_student_from_course(db=db, student_id=student_course.student_id, course_id=student_course.course_id)
