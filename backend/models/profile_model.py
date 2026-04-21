from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from db.database import Base
from datetime import datetime

class Profile(Base):
    __tablename__="profiles"

    id= Column(Integer, primary_key=True, index=True)
    user_id= Column(Integer, ForeignKey("users.id"))
    stream= Column(String(50))
    class_level=Column(String(50))
    created_at=Column(TIMESTAMP, default=datetime.utcnow())
