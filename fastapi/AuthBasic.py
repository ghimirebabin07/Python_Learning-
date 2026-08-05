from fastapi import FastAPI,Header,Depends,HTTPException
from fastapi.security import APIKeyHeader
from fastapi.security import APIKeyQuery
from jose import jwt 
from datetime import datetime,timedelta ,timezone


app = FastAPI()
def verify_token(token:str = Header()):
    if token != "mysecret":
        raise HTTPException(status_code=401,detail="Unauthorized user")
    return {"user":"Authorized"}

@app.get("/")

def get_user(user=Depends(verify_token)):
    return {
        "Message":"Welcome!",
        "User":user
    }
#API Key Authentication using APIkeyheader
API_KEY = "123sec"

api_key_header =  APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
    return api_key

@app.get("/products")
def products(api_key=Depends(verify_api_key)):
    return {
        "message": "Authenticated",
        "api_key": api_key
    }

#Using APIkeyQueries 

api_key_query = APIKeyQuery(name="api_key")

def verify_api_keyq(api_key: str = Depends(api_key_query)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
    return api_key

@app.get("/home")
def products(api_key=Depends(verify_api_key)):
    return {
        "message": "Authenticated",
        "api_key": api_key
    }


# Look for the API key in the request header
api_key_header = APIKeyHeader(name="api_key")


def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
    return api_key

# Protected route
@app.get("/home")
def home(api_key: str = Depends(verify_api_key)):
    return {
        "message": "Authenticated",
        "api_key": api_key
    }


#jwt 


SECREAT_KEY = "babin"

ALGORITHM = "HS256"
#create token 
def create_token(data:dict ):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc )+timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })

    token = jwt.encode(to_encode,SECREAT_KEY,algorithm=ALGORITHM)

    return token 
#login token 

@app.post("/login")
def login(username:str,password:str):
    if username != "admin" or password != "123":
        raise HTTPException(status_code=401,detail="Invalid username and password")
    token = create_token({
        "sub":username
    })
    return{
        "access_token":token
    }


def verify_token(token:str = Header(None)):

    try :
        payload = jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="invalid or expirse token")

@app.get("/secure")
def profile(user: str = Depends(verify_token)):
    return {
        "message": "secure data accessed:",
        "user": user
    }