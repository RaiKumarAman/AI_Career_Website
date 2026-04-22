from fastapi import FastAPI
from db.database import engine, Base
from models.user_model import User
from models.profile_model import Profile
from models.test_model import Test
from controllers.auth_controller import router as auth_router
from controllers.profile_controller import router as user_router
from controllers.psychometric_controller import router as psychometric_router
from controllers.subject_controller import router as subject_router
from controllers.test_controller import router as test_router


app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(psychometric_router)
app.include_router(subject_router)
app.include_router(test_router)

@app.get("/")
def home():
    return {"message":"""
    1. Backend Running
    2. Auth Ready
    3. Profile Ready
    4. Psychometric test Ready
    5. Subject Mapping Ready"""}


