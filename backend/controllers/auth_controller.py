from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user_schemas import UserCreate, UserLogin
from db.database import get_db
from services.auth_service import create_user, login_user

router=APIRouter()

@router.post("/signup")
def signup(user:UserCreate, db:Session=Depends(get_db)):
    new_user, error=create_user(db, user.name, user.email, user.password)

    if error:
        return HTTPException(status_code=400, detail=error)
    
    return {"message":"USer Created sucessfully"}

@router.post("/login")
def login(user: UserLogin, db:Session=Depends(get_db)):
    token,error=login_user(db, user.email, user.password)

    if error:
        return HTTPException(status_code=400, detail=error)
    return {"access_token":token}

