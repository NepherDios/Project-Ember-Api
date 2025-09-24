from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
    
class GeneralItem(Base):
    __tablename__ = "GeneralItem"
    
    general_item_id = Column(Integer, primary_key=True, index=True)
    effect = Column(String(50))
    effect_value = Column(Float, nullable=False)
    stack = Column(Integer, nullable=False)
    buy_price = Column(Integer)
    sell_price = Column(Integer)
    item_id = Column(Integer, ForeignKey("Item.item_id"), nullable=False)
    
    item = relationship('Item', back_populates='general_item')
