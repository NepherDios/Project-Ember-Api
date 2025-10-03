from typing import Optional, List
from pydantic import BaseModel

class QuestCreate(BaseModel):
    quest_name: str
    description: str
    target: int
    location: Optional[str] = None
    
class QuestUpdate(BaseModel):
    quest_name: Optional[str]
    description: Optional[str]
    target: Optional[int]
    location: Optional[str]
    
class QuestResponse(BaseModel):
    quest_id: int
    quest_name: str
    description: str
    target: int
    location: Optional[str] = None
    
    class Config:
        orm_mode = True

class QuestListResponse(BaseModel):
    quest: List[QuestResponse]