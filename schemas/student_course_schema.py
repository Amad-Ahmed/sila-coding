# schemas/student_course_schema.py
from pydantic import BaseModel

class StudentCourseCreate(BaseModel):
    student_id: int
    course_id: int

class StudentCourseDelete(BaseModel):
    student_id: int
    course_id: int


class StudentCourseRead(StudentCourseCreate):
    id: int