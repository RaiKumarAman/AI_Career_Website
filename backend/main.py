from fastapi import FastAPI
from db.database import engine, Base
from models.user_model import User
from models.profile_model import Profile
from controllers.auth_controller import router as auth_router
from controllers.profile_controller import router as user_router


app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
def home():
    return {"message":"Backend running, Auth System ready, Profile ready"}


