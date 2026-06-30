from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home ():
    return {"message":"Hello worl from fastapi venv"}