from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.saves import CreateSave, UpdateSave, SaveResponse
from crud.save import create_save, get_saves, update_saves, delete_save

router = APIRouter(prefix="/saves", tags=["Saves"])

@router.post("/", response_model=SaveResponse)
def create_save_route(data: CreateSave, db: Session = Depends(get_db)):
    save = create_save(db, data)
    return SaveResponse(
        save_id=save.save_id,
        player_id=save.player_id
    )

@router.get("/player/{player_id}", response_model=List[SaveResponse])
def get_saves_route(player_id: int, db: Session = Depends(get_db)):
    saves_list = get_saves(db, player_id)
    return [
        SaveResponse(
            save_id=s.save_id,
            player_id=s.player_id
        )
        for s in saves_list
    ]

@router.put("/{player_id}/slot/{save_slot}", response_model=SaveResponse)
def update_save_route(player_id: int, save_slot: int, data: UpdateSave, db: Session = Depends(get_db)):
    save = update_saves(db, player_id, save_slot, data)
    if not save:
        raise HTTPException(status_code=404, detail="Save not found")
    return SaveResponse(
        save_id=save.save_id,
        player_id=save.player_id
    )

@router.delete("/{player_id}/slot/{save_slot}", response_model=SaveResponse)
def delete_save_route(player_id: int, save_slot: int, db: Session = Depends(get_db)):
    save = delete_save(db, player_id, save_slot)
    if not save:
        raise HTTPException(status_code=404, detail="Save not found")
    return SaveResponse(
        save_id=save.save_id,
        player_id=save.player_id
    )
