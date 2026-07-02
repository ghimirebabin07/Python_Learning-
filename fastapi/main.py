from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home ():
    return {"message":"Hello worl from fastapi venv"}

@app.get("/About")
def About ():
    return {"Message":"welcome from the about page"}

@app.get("/products")
def get_items (limit: int =10):
    return{"Limits :":limit}


@app.get("/items")
def get_users(name:str=None, price:int=0):
    return{
        "Name:" :name,
        "Price":price
           }