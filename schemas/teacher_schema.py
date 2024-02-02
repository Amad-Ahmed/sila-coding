from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    dept_id: int

class TeacherRead(TeacherCreate):
    id: int
