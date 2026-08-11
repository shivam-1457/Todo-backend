from fastapi import FastAPI , APIRouter ,Depends , HTTPException,Response,status
from sqlalchemy.orm import Session
from .. import models,database,schemas,oauth2 ,database ,utils
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["authentication"]
)

@router.post("/login",response_model=schemas.LoginResponse)
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user_data = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid credentials")
    password_verify = utils.verify_password(user_credentials.password,user_data.password)
    if not password_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid password")
    token = oauth2.create_token_access({"user_id":user_data.id})
    return {"token":token, "token_type": "bearer"}
   
    
    
    
  