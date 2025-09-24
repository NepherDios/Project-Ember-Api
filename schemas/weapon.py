from pydantic import BaseModel
from typing import Optional
from enums.dmg_type import DmgType
from enums.weapon_type import WeaponType
from enums.equipment_placement import EquipmentPlacement

class WeaponCreate(BaseModel):
    weapon_type: WeaponType
    weapon_placement: EquipmentPlacement #Where it can be placed(Main-hand or Off-hand)
    weapon_dmg: int
    dmg_type: DmgType
    item_id: int

class WeaponUpdate(BaseModel):
    weapon_type: Optional[WeaponType]
    weapon_placement: Optional[EquipmentPlacement]
    weapon_dmg: Optional[int]
    dmg_type: Optional[DmgType]

class WeaponResponse(BaseModel):
    weapon_id: int
    weapon_type: WeaponType
    weapon_placement: EquipmentPlacement
    weapon_dmg: int
    dmg_type: DmgType
    item_id: int