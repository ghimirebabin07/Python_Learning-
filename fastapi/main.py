from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class user(BaseModel):
    name:str
    age:int

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

###Post request 
# class user(BaseModel):
#     name:str
#     age:int

# @app.post("/create-user")
# def create_user(user:user):
#     return{
#         "message":"user created",
#         "data":user
#     }


# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")
# def create_user(user:User):
#     return {
#         "message":"User created",
#         "data":user
#     }
    

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/Create_User")
def Create_User(user:User):
    return {
        "Message":"User created",
        "data":user
    }