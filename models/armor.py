from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
from enums.armor_type import ArmorType
from enums.equipment_placement import EquipmentPlacement

class Armor(Base):
    __tablename__ = "Armor"
    
    armor_id = Column(Integer, primary_key=True, index=True)
    armor_type = Column(Enum(ArmorType, name="armor_type_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    armor_placement = Column(Enum(EquipmentPlacement, name="armor_placement_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]))
    max_armor = Column(Integer, nullable=False)
    armor_regen = Column(Integer)
    armor_threshold = Column(Integer, nullable=False)
    item_id = Column(Integer, ForeignKey("Item.item_id"), nullable=False)
    
    #Relation To Item from Armor
    item = relationship('Item', back_populates='armor', uselist=False)