from fastapi import FastAPI,Depends,HTTPException,Header,httpx 
import time 
from jose import jwt
from datetime import datetime,timedelta,timezone
import asyncio 


app = FastAPI()

app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
                "Message":"Async Programming API "}

#auth jwt 

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=30)


@app.get("/fetch-data")
async def fetch_data():
    # Use an async client to make a non-blocking network call
    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com")
    return response.json()




@app.get("/user")
async def get_user():

    # Create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:

        # Send a GET request to another API
        # 'await' pauses ONLY this function while waiting
        # FastAPI can handle other requests during this time
        response = await client.get(
            "https://jsonplaceholder.typicode.com/users/1"
        )

    # Convert the JSON response into a Python dictionary
    user = response.json()

    # Return only the data we need
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    }