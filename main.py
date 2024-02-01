from fastapi import FastAPI
from database import engine  # Make sure your database engine is correctly imported
from sqlalchemy.ext.declarative import declarative_base
from routers.department_router import router as department_router


app = FastAPI()

app.include_router(department_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}
