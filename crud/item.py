from models.item import Item
from schemas.item import ItemCreate
from sqlalchemy.orm import Session

def create_item(session: Session, data: ItemCreate) -> Item:
    item = Item(**data.model_dump())
    
    session.add(item)
    session.commit()
    session.refresh(item)
    
    return item

def get_item(session: Session, item_id: int) -> Item | None:
    return session.query(Item).filter(Item.item_id == item_id).first()

def delete_item(session: Session, item_id: int) -> Item | None:
    item = session.query(Item).filter(Item.item_id == item_id).first()
    
    if item:
        session.delete(item)
        session.commit()

    return item
