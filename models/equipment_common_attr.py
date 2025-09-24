from sqlalchemy import Column, Integer, Boolean, Enum
from sqlalchemy.orm import relationship
from database import Base

from enums.rarity_type import RarityType


class EquipmentCommonAttr(Base):
    __tablename__ = "EquipmentCommonAttr"
    
    common_attr_id = Column(Integer, primary_key=True, index=True)
    buy_price = Column(Integer)
    sell_price = Column(Integer)
    rarity = Column(Enum(RarityType, name="rarity_type_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    equipment_tier = Column(Integer, nullable=False)
    equipped = Column(Boolean, nullable="False", default=False)
    
    #Relation to EquipmentCommonAttr from Item table
    items = relationship('Item', back_populates='equipment_common_attr', cascade="save-update", passive_deletes=True)