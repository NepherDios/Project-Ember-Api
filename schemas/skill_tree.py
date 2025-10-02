from typing import Optional
from pydantic import BaseModel

class CreateSkillTree(BaseModel):
    player_id: int
    skills: Optional[list[int]] = None
    
class UpdateSkillTree(BaseModel):
    skill_tree_id: Optional[int]
    player_id: Optional[int]
    skills: Optional[list[int]]
    
class SkilltreeResponse(BaseModel):
    skill_tree_id: int
    player_id: int
    skills: Optional[list[int]] = None