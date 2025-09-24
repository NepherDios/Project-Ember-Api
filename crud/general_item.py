from models.general_item import GeneralItem
from schemas.general_item import GeneralItemCreate
from sqlalchemy.orm import Session

def create_general_item(session: Session, data: GeneralItemCreate) -> GeneralItem:
    general_item = GeneralItem(**data.model_dump())
    
    session.add(general_item)
    session.commit()
    session.refresh(general_item)
    
    return general_item

def get_general_item(session: Session, general_item_id: int) -> GeneralItem | None:
    return session.query(GeneralItem).filter(GeneralItem.general_item_id == general_item_id).first()