from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database import get_db
from schemas.progress import ProgressCreate, ProgressUpdate, ProgressResponse
from crud.progress import (
    create_player_progress,
    update_player_progress,
    get_player_progress,
    get_best_score,
    delete_player_progress,
    delete_player_progresses,
    delete_players_progress,
    delete_all_players_progress
)

router = APIRouter(prefix="/progress", tags=["progress"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_progress(data: ProgressCreate, db: Session = Depends(get_db)):
    try:
        progress = create_player_progress(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return progress

@router.put("/{player_id}/{stage_id}", status_code=status.HTTP_200_OK)
def update_progress(player_id: int, stage_id: int, updated_data: ProgressUpdate, db: Session = Depends(get_db)):
    try:
        progress = update_player_progress(db, player_id, stage_id, updated_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress

@router.get("/{player_id}", status_code=status.HTTP_200_OK, response_model=ProgressResponse)
def read_player_progress(player_id: int, db: Session = Depends(get_db)):
    try:
        progress_list = get_player_progress(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return progress_list

@router.get("/{player_id}/{stage_id}/best_score", status_code=status.HTTP_200_OK)
def read_best_score(player_id: int, stage_id: int, db: Session = Depends(get_db)):
    try:
        score = get_best_score(db, player_id, stage_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return {"best_score": score}

@router.delete("/", status_code=status.HTTP_200_OK)
def remove_all_progress(db: Session = Depends(get_db)):
    try:
        deleted_count = delete_all_players_progress(db)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return {"deleted_count": deleted_count}

@router.delete("/{player_id}/{stage_id}", status_code=status.HTTP_200_OK)
def remove_progress(player_id: int, stage_id: int, db: Session = Depends(get_db)):
    try:
        progress = delete_player_progress(db, player_id, stage_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress

@router.delete("/player/{player_id}", status_code=status.HTTP_200_OK)
def remove_all_player_progress(player_id: int, db: Session = Depends(get_db)):
    try:
        deleted_count = delete_player_progresses(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return {"deleted_count": deleted_count}

@router.delete("/stage/{stage_id}", status_code=status.HTTP_200_OK)
def remove_stage_progress(stage_id: int, db: Session = Depends(get_db)):
    try:
        deleted_count = delete_players_progress(db, stage_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return {"deleted_count": deleted_count}

