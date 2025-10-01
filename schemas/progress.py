from typing import Optional
from pydantic import BaseModel
from enums.biome import Biome

class ProgressCreate(BaseModel):
    player_id: int
    stage_id: int
    current_biome: Biome
    stage_difficulty: Optional[int] = None # if not yet started ;D
    stage_best_score: Optional[int] = 0
    
class ProgressUpdate(BaseModel):
    current_biome: Optional[Biome]
    stage_difficulty: Optional[int]
    stage_best_score: Optional[int]
    
class ProgressResponse(BaseModel):
    player_id: int
    stage_id: int
    current_biome: Biome
    stage_difficulty: Optional[int] = None
    stage_best_score: Optional[int] = None