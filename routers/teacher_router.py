from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from schemas.teacher_schema import TeacherCreate, TeacherRead
import crud.crud_teacher as crud
from database import SessionLocal
import csv
import io


router = APIRouter()
router.tags = ["teachers"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint to create a new teacher
@router.post("/teachers/", response_model=TeacherRead, tags=["teachers"])
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db=db, teacher=teacher)


# endpoint to upload a CSV file
@router.post('/teachers/upload-csv/', tags=["teachers"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig") 
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        teacher = TeacherCreate(**row)
        crud.create_teacher(db=db, teacher=teacher)
    return {"message": "CSV has been processed"}


# endpoint to read teacher by its teacher id
@router.get("/teachers/{teacher_id}", response_model=TeacherRead, tags=["teachers"])
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_teacher(db, teacher_id=teacher_id)

# endpoint to read all teachers
@router.get("/teachers/", response_model=list[TeacherRead], tags=["teachers"])
def read_all_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teachers(db, skip=skip, limit=limit)

    
# endpoint to update a teacher by its teacher id
@router.put("/teachers/{teacher_id}", response_model=TeacherRead, tags=["teachers"])
def update_teacher_info(teacher_id: int, teacher: TeacherCreate, db: Session = Depends(get_db)):
    return crud.update_teacher(db, teacher_id=teacher_id, teacher_data=teacher)

# endpoint to delete a teacher by its teacher id
@router.delete("/teachers/{teacher_id}", tags=["teachers"])
def remove_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return crud.delete_teacher(db, teacher_id=teacher_id)
    
