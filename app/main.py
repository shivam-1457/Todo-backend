from fastapi import FastAPI , APIRouter
from .database import Base , get_db ,engine
from sqlalchemy.orm import Session
from .routers import auth,post,user
from . import models
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://todofron.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)

@app.get("/")
def home():
    return {"message":"Welcome, Go to the docs :-"}



