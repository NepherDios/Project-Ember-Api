from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database import get_db
from schemas.roll_stat import RollStatCreate
from crud.roll_stat import create_roll_stat, get_roll_stat

router = APIRouter(prefix="/roll_stats", tags=["roll_stat"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_roll_stat(data: RollStatCreate, db: Session = Depends(get_db)):
    try:
        stat = create_roll_stat(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return stat

@router.get("/{roll_stat_id}", status_code=status.HTTP_200_OK)
def read_roll_stat(roll_stat_id: int, db: Session = Depends(get_db)):
    try:
        stat = get_roll_stat(db, roll_stat_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not stat:
        raise HTTPException(status_code=404, detail="Roll stat not found")
    return stat
