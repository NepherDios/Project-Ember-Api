from typing import Optional
from pydantic import BaseModel

class AbilityCreate(BaseModel):
    player_id: int
    ability_name: str
    ability_key: Optional[str] = None
    ability_slot: Optional[int] = None


class AbilityUpdate(BaseModel):
    ability_name: Optional[str]
    ability_key: Optional[str]
    ability_slot: Optional[int]


class AbilityResponse(BaseModel):
    ability_id: int
    player_id: int
    ability_name: str
    ability_key: Optional[str] = None
    ability_slot: Optional[int] = None

    class Config:
        orm_mode = True