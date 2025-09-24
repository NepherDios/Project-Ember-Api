from typing import Optional
from pydantic import BaseModel

class GeneralItemCreate(BaseModel):
    effect: Optional[str] = None
    effect_value: Optional[float] = None
    stack: int = 1
    buy_price: Optional[int] = None
    sell_price: Optional[int] = None
    item_id: int
    
class GeneralItemUpdate(BaseModel):
    effect: Optional[str]
    effect_value: Optional[float]
    stack: Optional[int]
    buy_price: Optional[int]
    sell_price: Optional[int]

class GeneralItemResponse(BaseModel):
    general_item_id: int
    effect: Optional[str] = None
    effect_value: Optional[float] = None
    stack: int
    buy_price: Optional[int] = None
    sell_price: Optional[int] = None
    item_id: int