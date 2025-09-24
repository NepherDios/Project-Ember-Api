from typing import Optional
from pydantic import BaseModel
from enums.item_type import ItemType
from schemas.equipment_common_attr import EquipmentCommonAttrResponse

class ItemCreate(BaseModel):
    item_type: ItemType
    item_name: str
    common_attr_id: Optional[int] = None

class ItemResponse(BaseModel):
    item_id: int
    item_name: str
    item_type: ItemType
    common_attr_id: Optional[int] = None

class ItemDetailsWithCommonAttr(BaseModel):
    item_id: int
    item_name: Optional[str] = None
    item_type: ItemType
    common_attr: Optional[EquipmentCommonAttrResponse] = None

    model_config = {
        "from_attributes": True
    }