from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from schemas.armor import ArmorCreate, ArmorUpdate, ArmorResponse
from database import get_db
from crud.armor import create_armor, update_armor, get_armor

router = APIRouter(prefix="/armors", tags=["armors"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_armor(data: ArmorCreate, db: Session = Depends(get_db)):
    try:
        armor = create_armor(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invalid Data: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return armor


@router.get("/{armor_id}", status_code=status.HTTP_200_OK, response_model=ArmorResponse)
def read_armor(armor_id: int, db: Session = Depends(get_db)):
    try:
        armor = get_armor(db, armor_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not armor:
        raise HTTPException(status_code=404, detail="Armor not found")
    return armor


@router.put("/{armor_id}", status_code=status.HTTP_200_OK)
def update_armor_data(armor_id: int, updated_data: ArmorUpdate, db: Session = Depends(get_db)):
    try:
        armor = update_armor(db, armor_id, updated_data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invalid update: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not armor:
        raise HTTPException(status_code=404, detail="Armor not found")
    return armor
