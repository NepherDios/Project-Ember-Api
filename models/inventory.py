from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Inventory(Base):
    __tablename__ = "Inventory"
    
    player_id = Column(Integer, ForeignKey("Player.player_id"), primary_key=True, index=True)
    slot_id = Column(Integer, primary_key=True, nullable=False, index=True)
    item_id = Column(Integer, ForeignKey("Item.item_id"), nullable=False)
    
    player = relationship('Player', back_populates='inventory')
    item = relationship('Item', back_populates='inventory')
