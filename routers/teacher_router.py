from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.teacher_schema import TeacherCreate, TeacherRead
import crud.crud_teacher as crud
from database import SessionLocal

router = APIRouter()
router.tags = ["teachers"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/teachers/", response_model=TeacherRead, tags=["teachers"])
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db=db, teacher=teacher)

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
