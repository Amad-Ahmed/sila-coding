from pydantic import BaseModel

class TeacherCourseCreate(BaseModel):
    teacher_id: int
    course_id: int

class TeacherCourseRead(TeacherCourseCreate):
    id: int
