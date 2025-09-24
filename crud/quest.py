from models.quest import Quest
from schemas.quest import QuestCreate, QuestUpdate
from sqlalchemy.orm import Session

def create_quest(session: Session, data: QuestCreate) -> Quest:
    quest = Quest(**data.model_dump())
    
    session.add(quest)
    session.commit()
    session.refresh(quest)
    
    return quest


def update_quest(session: Session, quest_id: int, updated_data: QuestUpdate) -> Quest | None:
    quest = session.query(Quest).filter(Quest.quest_id == quest_id).first()
    
    if not quest:
        return None
    
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(quest, key, value)
        
    session.commit()
    session.refresh(quest)
    
    return quest


def get_quest(session: Session, quest_id: int) -> Quest | None:
    return session.query(Quest).filter(Quest.quest_id == quest_id).first()


def get_all_quests(session: Session) -> list[Quest] | None:
    return session.query(Quest).all()


def delete_quest(session: Session, quest_id: int) -> Quest | None:
    quest = session.query(Quest).filter(Quest.quest_id == quest_id).first()
    
    if quest:
        session.delete(quest)
        session.commit()

    return quest

def delete_all_quests(session: Session) -> Quest | None:
    quests = session.query(Quest).delete(synchronize_session=False)

    return quests