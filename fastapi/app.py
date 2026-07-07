from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     password:str

# class UserResponce(BaseModel):
#     name:str
#     age:int 

# @app.get("/user", response_model=UserResponce)
# def get_user():
#     return {
#         "name":"Babin",
#         "age":20,
#             "password":"1234"    }

@app.post("/user_created",status_code=status.HTTP_201_CREATED)
def user_created():
    return{
        "message":"user created"
    }

@app.get("/user")
def get_user():
    return {
        "status":"success",
        "message":"user created",
        "data":{
            "name":"babin",
            "age":"20"

        }
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found "
        )
    return{
        "id":1,
        "name":"babin"
    }