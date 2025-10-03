from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database import get_db
from schemas.player import PlayerCreate, PlayerUpdate, PlayerResponse, PlayersListResponse
from crud.player import (
    create_player,
    update_player,
    get_player,
    get_all_players,
    delete_player,
)

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_player(data: PlayerCreate, db: Session = Depends(get_db)):
    try:
        player = create_player(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return player

@router.put("/{player_id}", status_code=status.HTTP_200_OK, response_model=PlayerResponse)
def update_player_data(player_id: int, updated_data: PlayerUpdate, db: Session = Depends(get_db)):
    try:
        player = update_player(db, player_id, updated_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/{player_id}", status_code=status.HTTP_200_OK, response_model=PlayerResponse)
def read_player(player_id: int, db: Session = Depends(get_db)):
    try:
        player = get_player(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/", status_code=status.HTTP_200_OK, response_model=PlayersListResponse)
def read_all_players(db: Session = Depends(get_db)):
    try:
        players = get_all_players(db)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return players

@router.delete("/{player_id}", status_code=status.HTTP_200_OK)
def remove_player(player_id: int, db: Session = Depends(get_db)):
    try:
        player = delete_player(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
