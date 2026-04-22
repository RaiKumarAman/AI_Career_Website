from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, String
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from db.database import Base
from datetime import datetime

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    subjects = Column(ARRAY(String))
    questions = Column(JSONB)

    created_at = Column(TIMESTAMP, default=datetime.utcnow)