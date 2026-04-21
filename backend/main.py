from fastapi import FastAPI
from db.database import engine, Base
from models.user_model import User
from controllers.auth_controller import router as auth_router

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message":"Backend running, Auth System ready"}


