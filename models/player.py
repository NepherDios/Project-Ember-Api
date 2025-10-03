from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database import Base
from models.save import PlayerSave

from enums.player_class import PlayerClass

class Player(Base):
    __tablename__ = "Player"
    
    player_id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String(25), unique=True, index=True, nullable=False)
    player_class = Column(Enum(PlayerClass, name="class_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    level = Column(Integer, nullable=False)
    current_xp = Column(Integer, nullable=False)
    gold = Column(Integer, nullable=False)
    souls = Column(Integer, nullable=False)
    
    inventory = relationship('Inventory', back_populates='player', cascade="all, delete-orphan")
    ability = relationship('Ability', back_populates='player', cascade="all, delete-orphan")
    progress = relationship('Progress', back_populates='player', cascade="all, delete-orphan")
    quest_progress = relationship('QuestProgress', back_populates='player', cascade="all, delete-orphan")
    skill_tree = relationship('SkillTree', back_populates='player', cascade = "all, delete-orphan")
    player_saves = relationship('PlayerSave', back_populates='player', cascade="all, delete-orphan")