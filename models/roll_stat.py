from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from database import Base

from enums.roll_type import RollType

class RollStat(Base):
    __tablename__ = "RollStat"
    
    roll_stat_id = Column(Integer, primary_key=True, index=True)
    roll_type = Column(Enum(RollType, name="roll_type_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    
    armory_enchantments = relationship('ArmoryEnchantment', back_populates='roll_stat', cascade="all, delete-orphan")