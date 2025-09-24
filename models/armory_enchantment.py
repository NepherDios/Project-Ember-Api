from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ArmoryEnchantment(Base):
    __tablename__ = "ArmoryEnchantment"
    
    roll_stat_id = Column(Integer, ForeignKey("RollStat.roll_stat_id"), primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("Item.item_id"))
    rolled_value_1 = Column(Float)
    rolled_value_2 = Column(Float)
    
    roll_stat = relationship('RollStat', back_populates='armory_enchantments')
    item = relationship('Item', back_populates="armory_enchantments")