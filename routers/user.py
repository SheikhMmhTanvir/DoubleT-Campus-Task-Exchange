from fastapi import APIRouter, Depends
from database import Base, engine, get_db
from sqlalchemy.orm import Session
import models
from crud import create_user, get_user, get_update_user, delete_user
router=APIRouter(
    prefix="/users",
    tags=["Users"]
)
@router.post("/")
def user_create(name:str, email:str, db:Session=Depends(get_db)):
    return create_user(db=db, name=name, email=email)
@router.get("/{name}")
def user_get(name:str, db:Session=Depends(get_db)):
    user=get_user(db=db, name=name)
    return{"ID":user.id, "Name":user.name, "Email":user.email}
@router.put("/{id}")
def user_update(id:int, new_name:str, new_email:str, db:Session=Depends(get_db)):
    user=get_update_user(db=db, id=id, new_name=new_name, new_email=new_email)
    return user
@router.delete("/{id}")
def user_delete(id: int, db:Session=Depends(get_db)):
    user=delete_user(db=db, id=id)
