import jwt
from pwdlib import PasswordHash 
from dotenv import load_dotenv
from config import secret_key, algorithm, access_token_expire_time
from datetime import datetime, timedelta, timezone

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

