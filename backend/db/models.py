from sqlalchemy import Column, Integer, String, Text, DateTime
from backend.db.database import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    role = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)
