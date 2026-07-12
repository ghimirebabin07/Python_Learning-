from fastapi import FastAPI,status,HTTPException,Depends,Header,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import time
import sqlite3 
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session

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

# Middleware 
@app.middleware("http")
async def get_middleware(request:Request,call_next):
    print("Request Received")

    response =await call_next(request)

    print("Responce sent")
    return response     


@app.middleware("http")
async def log_time(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time()-start
    print(f"Path:{request.url.path} | Time:{process_time}")
   

    return response

#database integration 

conn = sqlite3.connect("test.db",check_same_thread=False)

cursor = conn.cursor ()
cursor.execute("""
 CREATE TABLE IF NOT EXISTS todos(
               id INTEGER PRIMARY KEY,
               title TEXT,
               completed TEXT
)
              
 """)
@app.get("/home")
def home():
    return {
        "message":"SQlite connected fine"
    }
# database integration using sqlalchemy 
# Database URL (SQLite database file)
DATABASE_URL = "sqlite:///./test.db"

# Create a connection (engine) to the database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite with FastAPI
)

# Create a session factory (used to create database sessions)
sessionLocal = sessionmaker(bind=engine)

# Base class for all database models (tables)
Base = declarative_base()


# Todo table (model)
class Todo(Base):
    __tablename__ = "todos"  # Database table name

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String)                              
    completed = Column(String)                          


# Create all tables if they don't already exist
Base.metadata.create_all(bind=engine)


# Dependency: provide a database session for each request
def get_db():
    db = sessionLocal()  # Open database session
    try:
        yield db         # Give the session to the route
    finally:
        db.close()       # Always close the session


@app.get("/")
def home(db: Session = Depends(get_db)):
    # FastAPI injects the database session automatically
    return {
        "message": "DB connected fine"
    }