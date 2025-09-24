from pydantic import BaseModel

class AccessoryCreate(BaseModel):
    item_id: int

class AccessoryResponse(BaseModel):
    accessory_id: int
    item_id: int