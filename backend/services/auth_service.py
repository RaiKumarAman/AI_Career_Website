from sqlalchemy.orm import Session
from models.user_model import User
from security import get_password_hash, verify_password
from security import create_access_token

def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email==email).first()

def create_user(db:Session, name:str, email:str, password:str):
    exisiting_user=get_user_by_email(db,email)
    if exisiting_user:
        return None, "User already exists"

    hashed_password=get_password_hash(password)

    user=User(
        name=name,
        email=email,
        password_hash=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user, None

def login_user(db:Session, email:str, password:str):
    user=get_user_by_email(db, email)
    if not user:
        return None, "User not Found"
    if not verify_password(password, user.password_hash):
        return None, "invalid password"
    token= create_access_token({"user_id":user.id})
    return token, None

    