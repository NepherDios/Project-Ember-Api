from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

from enums.item_type import ItemType

class Item(Base):
    __tablename__ = "Item"
    
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False, index=True)
    item_type = Column(Enum(ItemType, name="item_type_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False, index=True)
    common_attr_id = Column(Integer, ForeignKey("EquipmentCommonAttr.common_attr_id", ondelete="SET NULL"), nullable=True)

    #Relations to Item from other tables
    accessory = relationship('Accessory', back_populates='item', cascade='all, delete-orphan', uselist=False)
    armor = relationship('Armor', back_populates='item', cascade='all, delete-orphan', uselist=False)
    weapon = relationship('Weapon', back_populates='item', cascade='all, delete-orphan', uselist=False)
    general_item = relationship('GeneralItem', back_populates='item', cascade='all, delete-orphan', uselist=False)
    inventory = relationship('Inventory', back_populates='item', cascade='all, delete-orphan')
    armory_enchantments = relationship('ArmoryEnchantment', back_populates='item', cascade='all, delete-orphan')
    
    #Relation from Item to EquipmentCommonAttr table
    equipment_common_attr = relationship('EquipmentCommonAttr', back_populates='items', uselist=False)