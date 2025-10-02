from sqlalchemy.orm import Session
from models.save import Save
from schemas.saves import CreateSave, SaveResponse, UpdateSave

def create_save(session: Session, data: CreateSave) -> Save | None:
    save = Save(**data)
    
    session.add(save)
    session.commit()
    session.refresh(save)
    
    return save


def get_saves(session: Session, player_id: int) -> list[Save] | None:
    return session.query(Save).filter(Save.player_id == player_id).all()
    
    
def update_saves(session: Session, player_id: int, save_slot: int, updated_data: UpdateSave) -> Save | None:
    save = session.query(Save).filter(Save.player_id == player_id, Save.save_slot == save_slot).first()
    
    if not save:
        return None
    
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(save, key, value)
        
    session.commit()
    session.refresh(save)
    
    return save
    
def delete_save(session: Session, player_id: int, save_slot: int) -> Save | None:
    save = session.query(Save).filter(Save.player_id == player_id, Save.save_slot == save_slot).first()
    
    if save:
        session.delete(save)
        session.commit()

    return save