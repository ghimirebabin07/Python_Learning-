from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home ():
    return {"message":"Hello worl from fastapi venv"}

@app.get("/About")
def About ():
    return {"Message":"welcome from the about page"}

@app.get("/user")
def user ():
    return {"user":["Babin","Hari","Ram"]}