from fastapi import FastAPI

app = FastAPI()


# Get method (/ points to localhost)

@app.get("/")
def message():
    return {"Hello": "World"}


# Another get example. Notice that the URL folder has changed and has new parameters

@app.get("/login/{username}")
def message2(username: str):
    return f"Your username is: {username}"
