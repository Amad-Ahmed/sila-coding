from pydantic import BaseModel
from datetime import date

# Schema for student creation
class StudentCreate(BaseModel):
    name: str
    dept_id: int
    dob: date

# Schema for reading student data
class StudentRead(StudentCreate):
    id: int

