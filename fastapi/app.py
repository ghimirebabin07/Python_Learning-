from fastapi import FastAPI,status,HTTPException,Depends,Header
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponce(BaseModel):
    name:str
    age:int 

@app.get("/user", response_model=UserResponce)
def get_user():
    return {
        "name":"Babin",
        "age":20,
            "password":"1234"    }

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


class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name
        

# exception handling 
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException (
            status_code=401,
            detail="user not found"
        )
    return {
        "message":"user",
        "id":1,
        "name":"Babin"
    }

@app.exception_handler(UserNotFoundException)
def userNotFound(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"User {exc.name} not found"}
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name !="Babin":
        raise UserNotFoundException (name)
         
    return { "name":name}

# dependence 

def common_logic():
    return {
        "message":"Common Logic is executed"
    }
@app.get("/home")
def home(data = Depends(common_logic)):
    return data 
# dependencies reuseable logic 

def get_uset_data():
    return {
        "user":"Babin Ghimire"
    }

@app.get("/profile")
def profile(user = Depends(get_uset_data)):
    return user

@app.get("/dashboard")
def dashboard(user=Depends(get_uset_data)):
    return user

#Auth example 

def verify_token(token:str=Header(None)):
    if token != "mybabin":
        raise HTTPException(
            status_code=401, detail="User is unauthorized"
        )
    return {
        "user":"Authorized user "
    }

@app.get("/secure-data")
def secure_user(user = Depends(verify_token)):
    return{
           "message":"secure user accessed",
    "user":user
    }
    
    
        
 
        


