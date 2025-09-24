from models.armor import Armor
from schemas.armor import ArmorCreate, ArmorUpdate
from sqlalchemy.orm import Session

def create_armor(session: Session, data: ArmorCreate) -> Armor:
    armor = Armor(**data.model_dump())
    
    session.add(armor)
    session.commit()
    session.refresh(armor)
    
    return armor

def update_armor(session: Session, armor_id: int, updated_data: ArmorUpdate) -> Armor | None:
    armor = session.query(Armor).filter(Armor.armor_id == armor_id).first()
    
    if not armor:
        return None
    
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(armor, key, value)
        
    session.commit()
    session.refresh(armor)
    
    return armor

def get_armor(session: Session, armor_id: int) -> Armor | None:
    return session.query(Armor).filter(Armor.armor_id==armor_id).first()