from fastapi import FastAPI,Depends,HTTPException,Header
import time 
from jose import jwt
from datetime import datetime,timedelta,timezone
import asyncio 

app = FastAPI()

# app.get("/")
# async def home():
#     await asyncio.sleep(3)
#     return {
#                 "Message":"Async Programming API "}

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