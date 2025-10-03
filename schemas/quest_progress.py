from pydantic import BaseModel
from typing import Optional, List

class QuestProgressCreate(BaseModel):
    player_id: int
    quest_id: int
    completed: bool

class QuestProgressUpdate(BaseModel):
    completed: Optional[bool]

class QuestProgressResponse(BaseModel):
    player_id: int
    quest_id: int
    completed: bool
    
    class Config:
        orm_mode = True
    
class QuestProgressListResponse(BaseModel):
    quests_progress_list: List[QuestProgressResponse]