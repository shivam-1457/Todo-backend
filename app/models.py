from sqlalchemy import Column , INTEGER, String ,ForeignKey
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id=Column(INTEGER,nullable=False,primary_key=True)
    name=Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    
class Post(Base):
    
    __tablename__ = "posts"
    
    id =Column(INTEGER,nullable=False,primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at = Column(String)
    owner_id = Column(INTEGER,ForeignKey("users.id"), nullable=False)
    
    