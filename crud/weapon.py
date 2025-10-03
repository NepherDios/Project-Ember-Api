from models.weapon import Weapon
from schemas.weapon import WeaponCreate, WeaponUpdate
from sqlalchemy.orm import Session

def create_weapon(session: Session, data: WeaponCreate) -> Weapon:
    weapon = Weapon(**data.dict())
    
    session.add(weapon)
    session.commit()
    session.refresh(weapon)
    
    return weapon

def update_weapon(session: Session, weapon_id: int, updated_data: WeaponUpdate) -> Weapon | None:
    weapon = session.query(Weapon).filter(Weapon.weapon_id == weapon_id).first()
    
    if not weapon:
        return None
    
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(weapon, key, value)
        
    session.commit()
    session.refresh(weapon)
    
    return weapon
        

def get_weapon(session: Session, weapon_id: int) -> Weapon | None:
    return session.query(Weapon).filter(Weapon.weapon_id == weapon_id).first()