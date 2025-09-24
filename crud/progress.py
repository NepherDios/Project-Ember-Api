from models.progress import Progress
from schemas.progress import ProgressCreate, ProgressUpdate
from sqlalchemy.orm import Session

#Creates stage information when the players enter a new stage(finishes the previous one :P)
def create_player_progress(session: Session, data: ProgressCreate) -> Progress:
    progress = Progress(**data.model_dump())
    
    session.add(progress)
    session.commit()
    session.refresh(progress)
    
    return progress

#Updates a player stage progress(updates either from maintanance or when player finishes the stage only)
def update_player_progress(session: Session, player_id: int, stage_id: int, updated_data: ProgressUpdate) -> Progress | None:
    progress = session.query(Progress).filter(Progress.player_id == player_id, Progress.stage_id == stage_id).first()
    
    if not progress:
        return None
    
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(progress, key, value)
        
    session.commit()
    session.refresh(progress)
    
    return progress

#Gets the player progress from all stages
def get_player_progress(session: Session, player_id: int) -> list[Progress] | None:
    return session.query(Progress).filter(Progress.player_id == player_id).all()


#Gets the best score from a specific player stage progress
def get_best_score(session: Session, player_id: int, stage_id: int) -> int:
   progress = session.query(Progress).filter(Progress.player_id == player_id, Progress.stage_id == stage_id).first()
   
   return progress.stage_best_score if progress else 0


#Delete one stage progress from a specific player
def delete_player_progress(session: Session, player_id: int, stage_id: int) -> Progress | None:
    progress = session.query(Progress).filter(Progress.player_id == player_id, Progress.stage_id == stage_id).first()
    
    if progress:
        session.delete(progress)
        session.commit()
    
    return progress

#Deletes all stages progress from a specific player
def delete_player_progresses(session: Session, player_id: int) -> int:
    deleted_progresses_count = session.query(Progress).filter(Progress.player_id == player_id).delete(synchronize_session=False)
    session.commit()
    
    return  deleted_progresses_count #Returns the number of progresses deleted

#Deletes one specific stage progress from all players
def delete_players_progress(session: Session, stage_id: int) -> int:
    deleted_progresses_count = session.query(Progress).filter(Progress.stage_id == stage_id).delete(synchronize_session=False)
    session.commit()
    
    return deleted_progresses_count


#Delete all stages progress from all players
def delete_all_players_progress(session: Session) -> int:
    deleted_progresses_count = session.query(Progress).delete(synchronize_session=False)
    session.commit()
    
    return deleted_progresses_count #Returns the number of progresses deleted