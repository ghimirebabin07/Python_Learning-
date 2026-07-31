from fastapi import FastAPI,Depends,HTTPException,Header
import time 
from jose import jwt
from datetime import datetime,timedelta,timezone
import asyncio 
import httpx 


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

# Simulate fetching user information
async def get_user():

    print("Fetching user...")

    # Pretend the database takes 2 seconds
    await asyncio.sleep(2)

    print("User fetched!")

    return {
        "name": "Babin",
        "age": 20
    }


# Simulate fetching orders
async def get_orders():

    print("Fetching orders...")

    await asyncio.sleep(2)

    print("Orders fetched!")

    return [
        "Laptop",
        "Keyboard",
        "Mouse"
    ]


# Simulate fetching payment history
async def get_payments():

    print("Fetching payments...")

    await asyncio.sleep(2)

    print("Payments fetched!")

    return {
        "total_paid": 2500
    }


@app.get("/profile")
async def profile():

    # Run ALL three functions at the same time
    user, orders, payments = await asyncio.gather(

        get_user(),

        get_orders(),

        get_payments()

    )

    return {

        "user": user,

        "orders": orders,

        "payments": payments

    }


# Simulate sending an email
async def send_email():

    print("Sending email...")

    # Pretend sending the email takes 5 seconds
    await asyncio.sleep(5)

    print("Email sent!")


@app.get("/order")
async def place_order():

    print("Order received")

    # Start sending the email in the background
    # This does NOT wait for the email to finish
    asyncio.create_task(send_email())

    print("Order saved")

    # Respond immediately to the client
    return {
        "message": "Order placed successfully!"
    }