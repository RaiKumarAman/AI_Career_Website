from sqlalchemy import Integer, String, TIMESTAMP, Column, Text, ForeignKey
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

class Recommendation(Base):
    __tablename__="recommendations"

    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"))
    test_id=Column(Integer, ForeignKey("tests.id"))

    career=Column(Text)
    secondary_careers = Column(ARRAY(Text))
    exams = Column(ARRAY(Text))
    feedback = Column(Text)

    created_at = Column(TIMESTAMP, default=datetime.utcnow)

