from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database import get_db
from schemas.quest import QuestCreate, QuestUpdate
from crud.quest import create_quest, update_quest, get_quest, get_all_quests, delete_quest, delete_all_quests

router = APIRouter(prefix="/quests", tags=["quest"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_quest(data: QuestCreate, db: Session = Depends(get_db)):
    try:
        quest = create_quest(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return quest

@router.put("/{quest_id}", status_code=status.HTTP_200_OK)
def modify_quest(quest_id: int, updated_data: QuestUpdate, db: Session = Depends(get_db)):
    try:
        quest = update_quest(db, quest_id, updated_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest

@router.get("/{quest_id}", status_code=status.HTTP_200_OK)
def read_quest(quest_id: int, db: Session = Depends(get_db)):
    try:
        quest = get_quest(db, quest_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest

@router.get("/", status_code=status.HTTP_200_OK)
def read_all_quests(db: Session = Depends(get_db)):
    try:
        quests = get_all_quests(db)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return quests

@router.delete("/", status_code=status.HTTP_200_OK)
def remove_all_quests(db: Session = Depends(get_db)):
    try:
        deleted_quests = delete_all_quests(db)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return {"deleted_count": deleted_quests}


@router.delete("/{quest_id}", status_code=status.HTTP_200_OK)
def remove_quest(quest_id: int, db: Session = Depends(get_db)):
    try:
        quest = delete_quest(db, quest_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest