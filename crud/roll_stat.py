from models.roll_stat import RollStat
from schemas.roll_stat import RollStatCreate
from sqlalchemy.orm import Session

def create_roll_stat(session: Session, data: RollStatCreate) -> RollStat:
    roll_stat = RollStat(**data.dict())
    
    session.add(roll_stat)
    session.commit()
    session.refresh(roll_stat)
    
    return roll_stat

def get_roll_stat(session: Session, roll_stat_id: int) -> RollStat | None:
    return session.query(RollStat).filter(RollStat.roll_stat_id == roll_stat_id).first()