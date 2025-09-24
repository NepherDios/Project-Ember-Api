from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class QuestProgress(Base):
    __tablename__ = "QuestProgress"
    
    player_id = Column(Integer, ForeignKey("Player.player_id"), primary_key=True, index=True)
    quest_id = Column(Integer, ForeignKey("Quest.quest_id"), primary_key=True, index=True)
    completed = Column(Boolean, nullable=False)
    
    #Relations to QuestProgress from Player and Quests Tables
    player = relationship('Player', back_populates='quest_progress')
    quest = relationship('Quest', back_populates='quest_progress')
