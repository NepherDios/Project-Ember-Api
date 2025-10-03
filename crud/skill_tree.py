from sqlalchemy.orm import Session
from models.skill_tree import SkillTree
from schemas.skill_tree import CreateSkillTree, UpdateSkillTree
from typing import List, Optional

def create_skill_tree(session: Session, data: CreateSkillTree) -> SkillTree:
    # Use .dict() to convert Pydantic model to dict
    skill_tree = SkillTree(**data.model_dump())
    
    session.add(skill_tree)
    session.commit()
    session.refresh(skill_tree)
    
    return skill_tree

def get_player_skill_trees(session: Session, player_id: int) -> List[SkillTree]:
    return session.query(SkillTree).filter(SkillTree.player_id == player_id).all()

def update_skill_tree(session: Session, skill_tree_id: int, updated_data: UpdateSkillTree) -> Optional[SkillTree]:
    skill_tree = session.query(SkillTree).filter(SkillTree.skill_tree_id == skill_tree_id).first()
    
    if not skill_tree:
        return None
    
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(skill_tree, key, value)
        
    session.commit()
    session.refresh(skill_tree)
    
    return skill_tree

def delete_skill_tree(session: Session, skill_tree_id: int) -> Optional[SkillTree]:
    skill_tree = session.query(SkillTree).filter(SkillTree.skill_tree_id == skill_tree_id).first()
    
    if skill_tree:
        session.delete(skill_tree)
        session.commit()

    return skill_tree
