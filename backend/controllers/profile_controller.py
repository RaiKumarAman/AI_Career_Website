from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.profile_schemas import ProfileCreate
from services.profile_service import create_profile, get_profile
from security import get_current_user

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/profile")
def create(
    data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    profile = create_profile(db, current_user.id, data)
    return {"message": "Profile saved", "profile": profile}


@router.get("/profile")
def read(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    profile = get_profile(db, current_user.id)

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return {
        "profile_exists": bool(profile),
        "profile": profile
    }

