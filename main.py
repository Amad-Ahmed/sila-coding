from fastapi import FastAPI
from database import engine
from models.department import Base

from routers.department_router import router as department_router
from routers.student_router import router as student_router


app = FastAPI()

# Only call this once, after all models have been imported
Base.metadata.create_all(bind=engine)

app.include_router(department_router)
app.include_router(student_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
