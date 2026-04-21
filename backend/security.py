import jwt
from pwdlib import PasswordHash 
from dotenv import load_dotenv
from config import secret_key, algorithm, access_token_expire_time
from datetime import datetime, timedelta, timezone
from fastapi import Header, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from config import secret_key, algorithm
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user_model import User

load_dotenv(override=True)

password_hash=PasswordHash.recommended()

def get_password_hash(password:str):
    return password_hash.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data:dict):
    to_encode=data.copy()
    
    expire=datetime.now() + timedelta(minutes=access_token_expire_time)
    
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)


security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    try:
        token = credentials.credentials  
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        user_id = payload.get("user_id")

        if user_id is None:
            raise Exception()

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user