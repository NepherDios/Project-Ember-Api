from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from database import Base

class SkillTree(Base):
    __tablename__ = "SkillTree"
    
    skill_tree_id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("Player.player_id"), index=True)
    skills = Column(ARRAY(Integer), default=list)
    
    player = relationship('Player', back_populates='skill_tree')