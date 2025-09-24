from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Accessory(Base):
    __tablename__ = "Accessory"
    
    accessory_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("Item.item_id"), nullable=False)
    
    #Relation to Item from Accessory
    item = relationship('Item', back_populates='accessory', uselist=False)