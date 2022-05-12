from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    lastname: str
    email: str
    phone: int


# Post method. We will use the class previously created (inheritage of BaseModel from pydantic)


@app.post("/student")
def save_student(student: Student):
    return f"Student {student.name} {student.lastname} saved!"
