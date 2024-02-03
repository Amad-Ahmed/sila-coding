from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.sql.sqltypes import DateTime



# Schema for student creation
class StudentCreate(BaseModel):
    name: str
    dept_id: int
    dob: datetime

# Schema for reading student data
class StudentRead(StudentCreate):
    id: int

