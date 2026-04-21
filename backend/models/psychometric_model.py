from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from db.database import Base
from datetime import datetime

class PsychometricResult(Base):
    __tablename__ = "psychometric_results"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    realistic = Column(Integer, default=0)
    investigative = Column(Integer, default=0)
    artistic = Column(Integer, default=0)
    social = Column(Integer, default=0)
    enterprising = Column(Integer, default=0)
    conventional = Column(Integer, default=0)

    top_1 = Column(String(50))
    top_2 = Column(String(50))

    created_at = Column(TIMESTAMP, default=datetime.utcnow())