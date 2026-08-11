
from fastapi import FastAPI , APIRouter ,Depends , HTTPException,Response,status
from sqlalchemy.orm import Session
from . import models,database,schemas,utils
from jose import JWTError,jwt
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from datetime import datetime , timedelta
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


security = HTTPBearer()

def create_token_access(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token:str):
    try:  
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload.get("user_id")
    except JWTError:
        return None

def get_current_user(credentials :HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user_id = verify_token(token)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"invalid token")
    return user_id
    
    

    

