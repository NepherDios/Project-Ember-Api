from pydantic import BaseModel
from enums.roll_type import RollType

class RollStatCreate(BaseModel):
    roll_type: RollType
    
class RollStatResponse(BaseModel):
    roll_stat_id: int
    roll_type: RollType