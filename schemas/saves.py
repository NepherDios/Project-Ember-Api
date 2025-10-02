from typing import Optional
from pydantic import BaseModel

class CreateSave(BaseModel):
    player_id: int
    
class UpdateSave(BaseModel):
    save_id: Optional[int]
    player_id: Optional[int]
    
class SaveResponse(BaseModel):
    save_id: int
    player_id: int