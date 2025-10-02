from sqlalchemy import Column, Integer, ForeignKey,SmallInteger, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class Save(Base):
    __tablename__ = "saves"
    
    save_id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('player.player_id'), index=True, nullable=False)
    save_slot = Column(SmallInteger, nullable=False)  # e.g., 1–3
    
    player = relationship('Player', back_populates='player_saves')
    
    __table_args__ = (UniqueConstraint('player_id', 'save_slot', name='uq_player_save_slot'),)
