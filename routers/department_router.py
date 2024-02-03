from fastapi import APIRouter, Depends,File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from schemas.department_schema import DepartmentCreate, DepartmentRead
from database import SessionLocal
import crud.crud_department as crud
import io
import csv

router = APIRouter()
router.tags = ["departments"]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/departments/", response_model=DepartmentRead, tags=["departments"])
def add_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)


@router.post('/departments/upload-csv/', tags=["departments"])
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    contents = contents.decode("utf-8-sig")  # Using "utf-8-sig" to automatically handle BOM
    file = io.StringIO(contents)
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the rest of your processing logic is correct
        department = DepartmentCreate(**row)
        crud.create_department(db=db, department=department)
    return {"message": "CSV has been processed"}



@router.get("/departments/{department_id}", response_model=DepartmentRead, tags=["departments"])
def read_department(department_id: int, db: Session = Depends(get_db)):
    return crud.get_department(db, department_id=department_id)

@router.put("/departments/{department_id}", response_model=DepartmentRead, tags=["departments"])
def update_department(department_id: int, department: DepartmentCreate, db: Session = Depends(get_db)):
    return crud.update_department(db, department_id=department_id, department_update=department)

@router.delete("/departments/{department_id}", tags=["departments"])
def delete_department(department_id: int, db: Session = Depends(get_db)):
    return crud.delete_department(db, department_id=department_id)

