from sqlalchemy.orm import Session
from models.save import PlayerSave
from schemas.saves import CreateSave, UpdateSave

def create_save(session: Session, data: CreateSave) -> PlayerSave | None:
    save = PlayerSave(**data.dict())
    
    session.add(save)
    session.commit()
    session.refresh(save)
    
    return save


def get_saves(session: Session, player_id: int) -> list[PlayerSave] | None:
    return session.query(PlayerSave).filter(PlayerSave.player_id == player_id).all()
    
    
def update_saves(session: Session, player_id: int, save_slot: int, updated_data: UpdateSave) -> PlayerSave | None:
    save = session.query(PlayerSave).filter(PlayerSave.player_id == player_id, PlayerSave.save_slot == save_slot).first()
    
    if not save:
        return None
    
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(save, key, value)
        
    session.commit()
    session.refresh(save)
    
    return save
    
def delete_save(session: Session, player_id: int, save_slot: int) -> PlayerSave | None:
    save = session.query(PlayerSave).filter(PlayerSave.player_id == player_id, PlayerSave.save_slot == save_slot).first()
    
    if save:
        session.delete(save)
        session.commit()

    return save