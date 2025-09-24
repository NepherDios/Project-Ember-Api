from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

from enums.equipment_placement import EquipmentPlacement
from enums.weapon_type import WeaponType
from enums.dmg_type import DmgType

class Weapon(Base):
    __tablename__ = "Weapon"
    
    weapon_id = Column(Integer, primary_key=True, index=True)
    weapon_placement = Column(Enum(EquipmentPlacement, name="equipment_placement_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]))
    weapon_dmg = Column(Integer, nullable=False)
    weapon_type = Column(Enum(WeaponType, name="weapon_type_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    dmg_type = Column(Enum(DmgType, name="dmg_type_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    item_id = Column(Integer, ForeignKey("Item.item_id"), nullable=False)
    
    #Relation to Item from Weapon
    item = relationship('Item', back_populates='weapon', uselist=False)