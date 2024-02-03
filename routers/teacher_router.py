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

# @router.post("/teachers/", response_model=TeacherRead, tags=["teachers"])
# def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
#     return crud.create_teacher(db=db, teacher=teacher)
@router.post("/teachers/", response_model=TeacherRead, tags=["teachers"])
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_teacher(db=db, teacher=teacher)
    except HTTPException as e:
        raise e


@router.post('/teachers/upload-csv/', tags=["teachers"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the rest of your processing logic is correct
        teacher = TeacherCreate(**row)
        crud.create_teacher(db=db, teacher=teacher)
    return {"message": "CSV has been processed"}



@router.get("/teachers/{teacher_id}", response_model=TeacherRead, tags=["teachers"])
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@router.put("/teachers/{teacher_id}", response_model=TeacherRead, tags=["teachers"])
def update_teacher_info(teacher_id: int, teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = crud.update_teacher(db, teacher_id=teacher_id, teacher_data=teacher)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@router.delete("/teachers/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["teachers"])
def remove_teacher(teacher_id: int, db: Session = Depends(get_db)):
    result = crud.delete_teacher(db, teacher_id=teacher_id)
    if not result.get("ok"):
        raise HTTPException(status_code=404, detail="Teacher not found")
