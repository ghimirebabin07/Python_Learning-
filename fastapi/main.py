from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# class user(BaseModel):
#     name:str
#     age:int

# @app.get("/")
# def home ():
#     return {"message":"Hello worl from fastapi venv"}

# @app.get("/About")
# def About ():
#     return {"Message":"welcome from the about page"}

# @app.get("/products")
# def get_items (limit: int =10):
#     return{"Limits :":limit}


# @app.get("/items")
# def get_users(name:str=None, price:int=0):
#     return{
#         "Name:" :name,
#         "Price":price
#            }

###Post request 
# class user(BaseModel):
#     name:str
#     age:int

# @app.post("/create-user")
# def create_user(user:user):
#     return{
#         "message":"user created",
#         "data":user
#     }


# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")
# def create_user(user:User):
#     return {
#         "message":"User created",
#         "data":user
#     }
    

# class Address(BaseModel):
#     city:str
#     pincode:int

# class User(BaseModel):
#     name:str
#     age:int
#     address:Address

# @app.post("/Create_User")
# def Create_User(user:User):
#     return {
#         "Message":"User created",
#         "data":user
#     }


# todos = []
# class Todo(BaseModel):
#     id : int
#     title:str
#     completed:bool

# @app.post("/todos")
# def create_todo(todo:Todo):
#     todos.append(todo)
#     return {"Message":"todo is added","data":todo}

# @app.get("/todos")
# def get_todos():
#     return todos

# @app.get("/todos/{todo_id}")
# def get_todo(todo_id:int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     return {"Error":"Todo not found "}

# @app.put("/todos/{todo_id}")
# def update_todo(todo_id: int, updated_todo: Todo):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:   # Assuming Todo has an 'id' field
#             todos[index] = updated_todo
#             return {
#                 "Message": "Data Updated",
#                 "Data": updated_todo
#             }

#     return {"Error": "Todo not found"}

# @app.delete("/todo/{todo_id}")
# def delete_todo(todo_id:int):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos.pop(index)
#             return {"message":"Data is Deleted"}
#     return {"Error":"todo not found"}

#path query and body params 
users = []
class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {"Message ":"User's created",
            "Data":user}

@app.put("/users/{user_id}")
def update_user(user_id:int, user:User,notify:bool=False):
    if user_id < len(users):
        users[user_id] = user
        return {
            "message":'user created ',
            "notify":notify,
            "data":user
        }
    return {"Error":"user not found"}
  