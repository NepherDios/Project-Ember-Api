from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database import get_db
from schemas.quest_progress import QuestProgressCreate, QuestProgressUpdate
from crud.quest_progress import (
    create_player_quest_progress,
    update_player_quest_progress,
    get_player_quest_progress,
    get_all_player_quest_progress
)

router = APIRouter(prefix="/quest_progress", tags=["quest_progress"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_quest_progress(data: QuestProgressCreate, db: Session = Depends(get_db)):
    try:
        progress = create_player_quest_progress(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return progress

@router.put("/{player_id}", status_code=status.HTTP_200_OK)
def modify_quest_progress(player_id: int, updated_data: QuestProgressUpdate, db: Session = Depends(get_db)):
    try:
        progress = update_player_quest_progress(db, player_id, updated_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not progress:
        raise HTTPException(status_code=404, detail="Quest progress not found")
    return progress

@router.get("/{player_id}/{quest_id}", status_code=status.HTTP_200_OK)
def read_quest_progress(player_id: int, quest_id: int, db: Session = Depends(get_db)):
    try:
        progress = get_player_quest_progress(db, player_id, quest_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not progress:
        raise HTTPException(status_code=404, detail="Quest progress not found")
    return progress

@router.get("/{player_id}", status_code=status.HTTP_200_OK)
def read_all_quest_progress(player_id: int, db: Session = Depends(get_db)):
    try:
        progress_list = get_all_player_quest_progress(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return progress_list
