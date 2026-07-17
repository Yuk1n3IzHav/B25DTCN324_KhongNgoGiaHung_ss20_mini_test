from fastapi import FastAPI
from router import student

app = FastAPI()

app.include_router(student)