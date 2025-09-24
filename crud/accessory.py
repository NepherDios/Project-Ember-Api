from models.accessory import Accessory
from schemas.accessory import AccessoryCreate
from sqlalchemy.orm import Session

def create_accessory(session: Session, data: AccessoryCreate) -> Accessory:
    accessory = Accessory(**data.model_dump())
    
    session.add(accessory)
    session.commit()
    session.refresh(accessory)
    
    return accessory

def get_accessory(session: Session, accessory_id: int) -> Accessory | None:
    return session.query(Accessory).filter(Accessory.accessory_id == accessory_id).first()