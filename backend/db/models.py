from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from db.database import Base, engine
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    role = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

Base.metadata.create_all(bind=engine)