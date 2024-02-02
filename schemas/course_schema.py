from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str
    description: str
    dept_id: int
    credits: int

class CourseRead(CourseCreate):
    id: int
