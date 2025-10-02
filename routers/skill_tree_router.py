from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.skill_tree import CreateSkillTree, UpdateSkillTree, SkilltreeResponse
from crud.skill_tree import create_skill_tree, get_skill_trees, update_skill_tree, delete_skill_tree

router = APIRouter(prefix="/player-skill-tree", tags=["SkillTrees"])

# Create a new skill tree
@router.post("/", response_model=SkilltreeResponse)
def create_skilltree_route(data: CreateSkillTree, db: Session = Depends(get_db)):
    skill_tree = create_skill_tree(db, data)
    return SkilltreeResponse(
        skill_tree_id=skill_tree.skill_tree_id,
        player_id=skill_tree.player_id,
        skills=skill_tree.skills
    )

# Get all skill trees for a player
@router.get("/player/{player_id}", response_model=List[SkilltreeResponse])
def get_skilltrees_route(player_id: int, db: Session = Depends(get_db)):
    skill_trees = get_skill_trees(db, player_id)
    return [
        SkilltreeResponse(
            skill_tree_id=st.skill_tree_id,
            player_id=st.player_id,
            skills=st.skills
        )
        for st in skill_trees
    ]

# Update a skill tree (only skills field)
@router.put("/{skill_tree_id}", response_model=SkilltreeResponse)
def update_skilltree_route(skill_tree_id: int, data: UpdateSkillTree, db: Session = Depends(get_db)):
    skill_tree = update_skill_tree(db, skill_tree_id, data)
    if not skill_tree:
        raise HTTPException(status_code=404, detail="Skill tree not found")
    return SkilltreeResponse(
        skill_tree_id=skill_tree.skill_tree_id,
        player_id=skill_tree.player_id,
        skills=skill_tree.skills
    )

# Delete a skill tree
@router.delete("/{skill_tree_id}", response_model=SkilltreeResponse)
def delete_skilltree_route(skill_tree_id: int, db: Session = Depends(get_db)):
    skill_tree = delete_skill_tree(db, skill_tree_id)
    if not skill_tree:
        raise HTTPException(status_code=404, detail="Skill tree not found")
    return SkilltreeResponse(
        skill_tree_id=skill_tree.skill_tree_id,
        player_id=skill_tree.player_id,
        skills=skill_tree.skills
    )
