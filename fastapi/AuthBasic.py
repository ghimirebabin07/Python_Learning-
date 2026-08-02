from fastapi import FastAPI,Header,Depends,HTTPException


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
