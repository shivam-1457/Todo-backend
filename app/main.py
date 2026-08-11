from fastapi import FastAPI , APIRouter
from .database import Base , get_db ,engine
from sqlalchemy.orm import Session
from .routers import auth,post,user
from . import models
import psycopg2

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# app.include_router(auth.router)
# app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)

@app.get("/")
def home():
    return {"message":"hello world"}



