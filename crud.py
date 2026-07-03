from models import User
from sqlalchemy.orm import Session


def create_user(db:Session, name:str, email:str):
    db_user=User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_update_user(db:Session, id:int,new_name:str, new_email:str):
    db_user=db.query(User).filter(User.id==id).first()
    if db_user:
        db_user.name=new_name
        db_user.email=new_email
        db.commit()
        db.refresh(db_user)  
    return db_user  
def get_user(db:Session, name:str):
    return db.query(User).filter(User.name==name).first()
def delete_user(db:Session, id:int):
    db_user=db.query(User).filter(User.id==id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user