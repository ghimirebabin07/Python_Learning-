from fastapi import FastAPI,Depends
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base,Session 

app = FastAPI() 

DATABASE_URL = "sqlite:///./crud.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)
sessionLocal = sessionmaker(bind = engine)
Base = declarative_base() 

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(String)


Base.metadata.create_all(bind = engine)

def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
        db.close

#create api 

@app.post("/todos")
def create_db(title:str, db:Session = Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo created",
        "data":todo
    }