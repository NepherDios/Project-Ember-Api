from pydantic import BaseModel
from typing import Optional, Dict
from enums.item_type import ItemType
from schemas.item import ItemDetailsWithCommonAttr

class InventoryCreate(BaseModel):
    player_id: int
    slot_id: int
    item_id: int

class InventoryUpdate(BaseModel):
    item_id: int
    slot_id: int

class InventoryItemResponse(BaseModel):
    player_id: int
    slot_id: int
    item_id: int

    model_config = {
        "from_attributes": True
    }

class InventoryResponse(BaseModel):
    items: list[InventoryItemResponse]
    
class ItemDetails(BaseModel):
    item_id: int
    item_name: Optional[str] = None
    item_type: ItemType

    model_config = {
        "from_attributes": True
    }
    
class InventoryItemWithDetails(BaseModel):
    slot_id: int
    item: ItemDetails

    model_config = {
        "from_attributes": True
    }

class InventoryWithDetailsResponse(BaseModel):
    items: list[InventoryItemWithDetails]

class InventoryItemWithCommonAttr(BaseModel):
    slot_id: int
    item: ItemDetailsWithCommonAttr

    model_config = {
        "from_attributes": True
    }

class InventoryWithCommonAttrResponse(BaseModel):
    items: list[InventoryItemWithCommonAttr]
