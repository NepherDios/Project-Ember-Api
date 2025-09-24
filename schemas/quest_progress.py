from pydantic import BaseModel
from typing import Optional

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