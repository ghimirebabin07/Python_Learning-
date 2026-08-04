from fastapi import FastAPI,Header,Depends,HTTPException
from fastapi.security import APIKeyHeader
from fastapi.security import APIKeyQuery


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