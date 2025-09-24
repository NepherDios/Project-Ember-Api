from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class Ability(Base):
    __tablename__ = "Ability"
    
    ability_id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("Player.player_id"), nullable=False, index=True)
    ability_key = Column(String(20), unique=True)
    ability_slot = Column(Integer)
    
    player = relationship('Player', back_populates='ability')
    __table_args__ = (UniqueConstraint('player_id', 'ability_key', name='uq_player_ability_key'),)