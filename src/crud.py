from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []


class Student(BaseModel):
    id: str
    name: str
    lastname: str
    email: str
    phone: int


@app.get("/students")  # Get data
def get_students():
    return students


@app.get("/students/{id}")  # Search data
def get_students(id: str):
    for student in students:
        if student["id"] == id:
            return student
    return "Student not registered"


@app.post("/students")  # Add data
def save_student(student: Student):
    students.id = str(uuid4())  # Generates an id. See import uuid4
    students.append(student.dict())  # Adding data in a dictionary
    return "Student registered"


@app.put("/students/{id}")  # Modify data
def edit_student(updated_student: Student, id: str):
    for student in students:
        if student["id"] == id:
            student["name"] = student.name
            student["lastname"] = student.lastname
            student["email"] = student.email
            return "Student updated"
    return "Student doesn't exist"


@app.delete("/students/{id}")  # Delete data
def delete_student(id: str):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return "Student deleted"
    return "Student doesn't exist"
