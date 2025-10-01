from pydantic import BaseModel
from enums.armor_type import ArmorType
from enums.equipment_placement import EquipmentPlacement
from typing import Optional

class ArmorCreate(BaseModel):
    item_id: int
    armor_type: ArmorType
    armor_placement: EquipmentPlacement
    max_armor: int
    armor_regen: Optional[float] = None
    armor_threshold: int

class ArmorUpdate(BaseModel):
    armor_type: Optional[ArmorType]
    armor_placement: Optional[EquipmentPlacement]
    max_armor: Optional[int]
    armor_regen: Optional[float]
    armor_threshold: Optional[int]

class ArmorResponse(BaseModel):
    armor_id: int
    item_id: int
    armor_type: ArmorType
    armor_placement: EquipmentPlacement
    max_armor: int
    armor_regen: Optional[float] = None
    armor_threshold: int