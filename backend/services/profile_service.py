from sqlalchemy.orm import Session
from models.user_model import User
from models.profile_model import Profile

def create_profile(db:Session, user_id: int , data):
    exisiting_profile=db.query(Profile).filter(Profile.user_id==user_id).first()
    if exisiting_profile:
        profile.stream=data.stream
        profile.class_level=data.class_level
    else:
        profile=Profile(
            user_id=user_id,
            stream=data.stream,
            class_level=data.class_level
        )
        db.add(profile)
    
    exisiting_user=db.query(User).filter(User.id==user_id).first()
    User.language=data.language

    db.commit()
    db.refresh(profile)

    return profile

def get_profile(db:Session, user_id:int):
    return db.query(Profile).filter(Profile.user_id==user_id).first()

