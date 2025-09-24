from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

from enums.biome import Biome

class Progress(Base):
    __tablename__ = "Progress"
    
    player_id = Column(Integer, ForeignKey("Player.player_id"), primary_key=True, index=True)
    stage_id = Column(Integer, primary_key=True, index=True)
    current_biome = Column(Enum(Biome, name="biome_enum", native_enum=True, values_callable=lambda enum_class: [e.value for e in enum_class]), nullable=False)
    stage_difficulty = Column(Integer)
    stage_best_score = Column(Integer)
    
    player = relationship('Player', back_populates="progress")