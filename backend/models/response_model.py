from sqlalchemy import Column, Integer, ForeignKey, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from db.database import Base
from datetime import datetime

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    test_id = Column(Integer, ForeignKey("tests.id"))

    user_answers = Column(JSONB)
    score = Column(Float)
    total_questions = Column(Integer)

    created_at = Column(TIMESTAMP, default=datetime.utcnow)