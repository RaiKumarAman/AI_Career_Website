from sqlalchemy.orm import Session
from models.user_model import User
from models.profile_model import Profile

from sqlalchemy.orm import Session
from models.user_model import User
from models.profile_model import Profile

def create_profile(db: Session, user_id: int, data):

    existing_profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if existing_profile:
        #use existing_profile
        existing_profile.stream = data.stream
        existing_profile.class_level = data.class_level
        profile = existing_profile
    else:
        profile = Profile(
            user_id=user_id,
            stream=data.stream,
            class_level=data.class_level
        )
        db.add(profile)

    # update user instance, not class
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user:
        existing_user.language = data.language

    db.commit()
    db.refresh(profile)

    return profile

def get_profile(db:Session, user_id:int):
    return db.query(Profile).filter(Profile.user_id==user_id).first()

