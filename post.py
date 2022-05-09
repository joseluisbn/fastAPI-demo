from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    lastname: str
    email: str
    phone: int


# Post method. We will use the class previously created (inheritage of BaseModel)

@app.post("/user")
def save_student(user: User):
    return f"Student {user.name} {user.lastname} saved!"
