from sqlalchemy import Column, Integer, String, TIMESTAMP
from db.database import Base
from datetime import datetime

class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(100))
    email=Column(String(100), unique=True, index=True)
    password_hash=Column(String)
    language=Column(String(10), default="en")
    created_at=Column(TIMESTAMP, default=datetime.utcnow())
