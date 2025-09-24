from pydantic import BaseModel
from enums.player_class import PlayerClass
from typing import Optional

class PlayerCreate(BaseModel):
    player_name: str
    player_class: PlayerClass
    souls: int = 0
    gold: int = 0
    level: int = 1
    current_xp: int = 0
    
class PlayerUpdate(BaseModel):
    player_name: Optional[str]
    player_class: Optional[PlayerClass]
    souls: Optional[int]
    gold: Optional[int]
    level: Optional[int]
    current_xp: Optional[int]
    
class PlayerResponse(BaseModel):
    player_id: int
    player_name: str
    player_class: PlayerClass
    souls: int
    gold: int
    level: int
    current_xp: int