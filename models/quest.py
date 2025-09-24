from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Quest(Base):
    __tablename__ = "Quest"
    
    quest_id = Column(Integer, primary_key=True, index=True)
    quest_name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    target = Column(Integer, nullable=False)
    location = Column(String(50))
    
    quest_progress = relationship('QuestProgress', back_populates='quest', cascade="all, delete-orphan")
