

from fastapi import FastAPI , APIRouter ,Depends , HTTPException,Response,status
from sqlalchemy.orm import Session
from .. import models,database,schemas,oauth2 ,utils
from pydantic import EmailStr

router = APIRouter(
    tags=["users"]
)

@router.post("/register")
def new_user(user:schemas.CreateUser,db:Session =Depends(database.get_db)):
    hash_password = utils.hash_password(user.password)
    user.password = hash_password
    new_user = models.User(**user.dict())
   
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"you have register successfully"}



    