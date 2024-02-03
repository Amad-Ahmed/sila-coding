from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from schemas.student_schema import StudentCreate, StudentRead
import crud.crud_student as crud
from database import SessionLocal
import csv
import io


router = APIRouter()
router.tags = ["students"]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=StudentRead, tags=["students"])
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)



@router.post('/students/upload-csv/', tags=["students"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the rest of your processing logic is correct
        student = StudentCreate(**row)
        crud.create_student(db=db, student=student)
    return {"message": "CSV has been processed"}



@router.get("/students/{student_id}", response_model=StudentRead,tags=["students"])
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id=student_id)

@router.get("/students/", tags=["students"])
def read_all_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)


@router.put("/students/{student_id}", response_model=StudentRead,tags=["students"])
def update_student_endpoint(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id=student_id, student_data=student)

@router.delete("/students/{student_id}", tags=["students"])
def delete_student_endpoint(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id=student_id)
