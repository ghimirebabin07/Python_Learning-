from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home ():
    return {"message":"Hello worl from fastapi venv"}

@app.get("/About")
def About ():
    return {"Message":"welcome from the about page"}

@app.get("/user/{user_id}")
def get_id(user_id:int):
    return {"user_id":user_id}

@app.get("/user")
def get_user(name):
    return {"Name":name}