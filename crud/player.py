from models.player import Player
from schemas.player import PlayerCreate, PlayerUpdate
from sqlalchemy.orm import Session


def create_player(session: Session, data: PlayerCreate) -> Player:
    player = Player(**data.dict())
    
    session.add(player)
    session.commit()
    session.refresh(player)
    
    return player


def update_player(session: Session, player_id: int, updated_data: PlayerUpdate) -> Player | None:
    player = session.query(Player).filter(Player.player_id == player_id).first()
    
    if not player:
        return None
    
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(player, key, value)
        
    session.commit()
    session.refresh(player)
    
    return player


def get_player(session: Session, player_id: int) -> Player | None:
    return session.query(Player).filter(Player.player_id == player_id).first()


def get_all_players(session: Session) -> list[Player] | None:
    return session.query(Player).all()


def delete_player(session: Session, player_id: int) -> Player | None:
    player = session.query(Player).filter(Player.player_id == player_id).first()
    
    if player:
        session.delete(player)
        session.commit()
        
    return player