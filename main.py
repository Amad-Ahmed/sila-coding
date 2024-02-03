from fastapi import FastAPI
from database import engine
from models.department import Base

from routers.department_router import router as department_router
from routers.student_router import router as student_router
from routers.course_router import router as course_router
from routers.student_course_router import router as student_course_router
from routers.teacher_router import router as teacher_router
from routers.teacher_course_router import router as teacher_course_router
from seed import seed_data
from dotenv import load_dotenv

load_dotenv()



# Only call this once, after all models have been imported
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(department_router)
app.include_router(student_router)
app.include_router(course_router)
app.include_router(student_course_router)
app.include_router(teacher_router)
app.include_router(teacher_course_router)




@app.get("/seed-data")
def root():
    seed_data()
    return {"message": "Data Seeded Successfully"}
