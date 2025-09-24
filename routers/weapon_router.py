from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database import get_db
from schemas.weapon import WeaponCreate, WeaponUpdate
from crud.weapon import create_weapon, update_weapon, get_weapon

router = APIRouter(prefix="/weapons", tags=["weapon"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_weapon(data: WeaponCreate, db: Session = Depends(get_db)):
    try:
        weapon = create_weapon(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return weapon

@router.put("/{weapon_id}", status_code=status.HTTP_200_OK)
def modify_weapon(weapon_id: int, updated_data: WeaponUpdate, db: Session = Depends(get_db)):
    try:
        weapon = update_weapon(db, weapon_id, updated_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon

@router.get("/{weapon_id}", status_code=status.HTTP_200_OK)
def read_weapon(weapon_id: int, db: Session = Depends(get_db)):
    try:
        weapon = get_weapon(db, weapon_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon
