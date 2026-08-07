from fastapi import FastAPI,Header,Depends,HTTPException
from fastapi.security import APIKeyHeader
from fastapi.security import APIKeyQuery
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from passlib.context import CryptContext
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


# JWT Settings using 0auth
SECRET_KEY = "babin"
ALGORITHM = "HS256"

# OAuth2 will expect the token to be obtained from /signin
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")


# Create JWT Token
def create_token(data: dict):
    to_encode = data.copy()

    # Token expires in 30 minutes
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update({
        "exp": expire
    })

    # Generate JWT
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# Verify JWT Token
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        # Decode JWT
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Get username
        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )


# User Login
@app.post("/signin")
def signin(form_data: OAuth2PasswordRequestForm = Depends()):

    # Check username and password
    if form_data.username != "admin" or form_data.password != "123":
        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )

    # Create JWT token
    access_token = create_token({
        "sub": form_data.username
    })

    # Return the token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Protected Route
@app.get("/dashboard")
def dashboard(current_user: str = Depends(verify_token)):
    # Runs only if the token is valid
    return {
        "message": f"Welcome {current_user}",
        "status": "Access Granted"
    }


# Another Protected Route
@app.get("/account")
def account(current_user: str = Depends(verify_token)):
    # Show user details after token verification
    return {
        "user": current_user,
        "email": "admin@example.com",
        "role": "Administrator"
    }


# Public Route
@app.get("/")
def home():
    # Anyone can access this route
    return {
        "message": "Welcome to FastAPI JWT Authentication"
    }