from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from schemas.course_schema import CourseCreate, CourseRead
import crud.crud_course as crud
from database import SessionLocal
import io
import csv

router = APIRouter()

router.tags = ["courses"]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoint to create a new course
@router.post("/courses/", response_model=CourseRead, tags=["courses"])
def create(course: CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)


# endpoint to upload a CSV file
@router.post('/courses/upload-csv/', tags=["courses"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
        file = io.StringIO(contents)
        reader = csv.DictReader(file)
        for row in reader:
            course = CourseCreate(**row)
            crud.create_course(db=db, course=course)
        return {"message": "CSV has been processed"}
    except HTTPException as e:
        return HTTPException(status_code=500, detail=f"Database error: {e}")


# endpoint to read a course by its id
@router.get("/courses/{course_id}", response_model=CourseRead, tags=["courses"])
def read(course_id: int, db: Session = Depends(get_db)):
    return crud.get_course(db=db, course_id=course_id)

# endpoint to read all courses
@router.get("/courses/", response_model=list[CourseRead], tags=["courses"])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_courses(db=db, skip=skip, limit=limit)

# endpoint to update a course by its id
@router.put("/courses/{course_id}", response_model=CourseRead, tags=["courses"])
def update(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    return crud.update_course(db=db, course_id=course_id, course_data=course)
    

# endpoint to delete a course by its id
@router.delete("/courses/{course_id}", tags=["courses"])
def delete(course_id: int, db: Session = Depends(get_db)):
    return crud.delete_course(db=db, course_id=course_id)
