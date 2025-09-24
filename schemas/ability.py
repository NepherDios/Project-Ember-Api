from typing import Optional
from pydantic import BaseModel

class AbilityCreate(BaseModel):
    player_id: int
    ability_key: Optional[str] = None
    ability_slot: Optional[int] = None


class AbilityUpdate(BaseModel):
    ability_key: Optional[str]
    ability_slot: Optional[int]


class AbilityResponse(BaseModel):
    ability_id: int
    player_id: int
    ability_key: Optional[str] = None
    ability_slot: Optional[int] = None

    model_config = {
        "from_attributes": True
    }