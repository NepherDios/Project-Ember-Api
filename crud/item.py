from models.item import Item
from schemas.item import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session

def create_item(session: Session, data: ItemCreate) -> Item:
    item = Item(**data.model_dump())
    
    session.add(item)
    session.commit()
    session.refresh(item)
    
    return item


def get_item(session: Session, item_id: int) -> Item | None:
    return session.query(Item).filter(Item.item_id == item_id).first()


def update_item(session: Session, item_id: int, updated_data: ItemUpdate) -> Item | None:
    item = get_item(session, item_id)
    
    if not item:
        return None
    else:
        for key, value in updated_data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

    session.commit()
    session.refresh(item)
        
    return item


def delete_item(session: Session, item_id: int) -> Item | None:
    item = get_item(session, item_id)
    
    if item:
        session.delete(item)
        session.commit()

    return item
