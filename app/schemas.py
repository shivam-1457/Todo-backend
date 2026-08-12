from pydantic import  BaseModel,EmailStr

class CreateUser(BaseModel):
    id:int
    name:str
    email :EmailStr
    password:str
    
class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    class Config:
        orm_mode :True
class PostCreate(BaseModel):
    id:int
    title:str
    content:str
    
class PostResponse(BaseModel):
    id:int
    title:str
    content:str
    owner_id:int
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    email:EmailStr
    password:str
class LoginResponse(BaseModel):
    token :str
    token_type:str
    class Config:
        orm_mode = True
class PostUpdate(BaseModel):
    id:int
    title:str
    content:str

    
   

    
