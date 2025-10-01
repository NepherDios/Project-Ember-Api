from typing import Optional
from pydantic import BaseModel
from enums.rarity_type import RarityType

class EquipmentCommonAttrCreate(BaseModel):
    buy_price: Optional[int] = None
    sell_price: Optional[int] = None
    rarity: RarityType
    equipment_tier: int
    equipped: Optional[bool] = False

class EquipmentCommonAttrUpdate(BaseModel):
    buy_price: Optional[int]
    sell_price: Optional[int]
    rarity: Optional[RarityType]
    equipment_tier: Optional[int]
    equipped: Optional[bool]

class EquipmentCommonAttrResponse(BaseModel):
    common_attr_id: int
    buy_price: Optional[int] = None
    sell_price: Optional[int] = None
    rarity: RarityType
    equipment_tier: int
    equipped: bool
    
    model_config = {
        "from_attributes": True
    }