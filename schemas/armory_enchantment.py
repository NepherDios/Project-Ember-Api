from pydantic import BaseModel
from typing import Optional

class ArmoryEnchantmentCreate(BaseModel):
    roll_stat_id: int
    item_id: int
    rolled_value_1: float
    rolled_value_2: float

class ArmoryEnchantmentUpdate(BaseModel):
    rolled_value_1: Optional[float]
    rolled_value_2: Optional[float]

class ArmoryEnchantmentResponse(BaseModel):
    item_id: int
    roll_stat_id: int
    rolled_value_1: float
    rolled_value_2: float