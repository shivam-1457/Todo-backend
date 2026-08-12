
from fastapi import FastAPI , APIRouter ,Depends , HTTPException,Response,status 
from typing import List
from sqlalchemy.orm import Session
from .. import models,database,schemas,oauth2 ,database ,utils


router = APIRouter(
    tags=["posts"]
)

@router.get("/profile",response_model=schemas.UserResponse)
def see_profile(db:Session = Depends(database.get_db) ,current_user = Depends(oauth2.get_current_user) ):
    profile = db.query(models.User).filter(models.User.id == current_user).first()
    return profile
    

@router.post("/createpost")
def create_post(post:schemas.PostCreate,db:Session =Depends(database.get_db),current_user = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.dict(),owner_id = current_user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message":"your post created successfully"}

    
    
@router.get("/getpost",response_model=List[schemas.PostResponse])
def get_post(db:Session = Depends(database.get_db),current_user = Depends(oauth2.get_current_user)):
    my_posts = db.query(models.Post).filter(models.Post.owner_id == current_user).all()
    return my_posts



@router.put("/updatepost")
def update_post(updated_post:schemas.PostUpdate, db:Session=Depends(database.get_db),current_user = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id ==updated_post.id, models.Post.owner_id == current_user).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found")
    post.title = updated_post.title
    post.content = updated_post.content
    db.commit()
    db.refresh(post)
    return {"message":"your post updated successfully"}

@router.delete("/deletepost/{id}")
def delete_post(id:int,db:Session = Depends(database.get_db),user_id = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id, models.Post.owner_id == user_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found")
    db.delete(post)
    db.commit()
    return {"message": f"your post id {id} deleted successfully"}
   