from models.quest_progress import QuestProgress
from schemas.quest_progress import QuestProgressCreate, QuestProgressUpdate
from sqlalchemy.orm import Session

#Creates the player quest progress once initiated
def create_player_quest_progress(session: Session, data: QuestProgressCreate) -> QuestProgress:
    quest_progress = QuestProgress(**data.dict())
    
    session.add(quest_progress)
    session.commit()
    session.refresh(quest_progress)
    
    return quest_progress

def update_player_quest_progress(session: Session, player_id: int, updated_data: QuestProgressUpdate) -> QuestProgress | None:
    quest_progress = session.query(QuestProgress).filter(QuestProgress.player_id == player_id).first()
    
    if not quest_progress:
        return None
    
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(quest_progress, key, value)
        
    session.commit()
    session.refresh(quest_progress)
    
    return quest_progress

#Gets the player specific quest
def get_player_quest_progress(session: Session, player_id: int, quest_id: int) -> QuestProgress | None:
    return session.query(QuestProgress).filter(QuestProgress.player_id == player_id, QuestProgress.quest_id == quest_id).first()

#Gets the progress of all the specific player quests
def get_all_player_quest_progress(session: Session, player_id: int) -> list[QuestProgress] | None:
    return session.query(QuestProgress).filter(QuestProgress.player_id == player_id).all()