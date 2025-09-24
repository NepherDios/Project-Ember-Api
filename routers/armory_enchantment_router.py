from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from database import get_db
from schemas.armory_enchantment import ArmoryEnchantmentCreate, ArmoryEnchantmentUpdate, ArmoryEnchantmentResponse
from crud.armory_enchantment import (
    create_armory_enchantment,
    update_armory_enchantment,
    get_armory_enchantment,
    get_armory_enchantments,
    remove_enchantment,
    remove_all_enchantments
)

router = APIRouter(prefix="/armory_enchantments", tags=["armory_enchantments"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_enchantment(data: ArmoryEnchantmentCreate, db: Session = Depends(get_db)):
    try:
        enchantment = create_armory_enchantment(db, data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return enchantment


@router.put("/{item_id}/{roll_stat_id}", status_code=status.HTTP_200_OK)
def update_enchantment(item_id: int, roll_stat_id: int, updated_data: ArmoryEnchantmentUpdate, db: Session = Depends(get_db)):
    try:
        enchantment = update_armory_enchantment(db, item_id, roll_stat_id, updated_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not enchantment:
        raise HTTPException(status_code=404, detail="Enchantment not found")
    return enchantment


@router.get("/{item_id}/{roll_stat_id}", status_code=status.HTTP_200_OK, response_model=ArmoryEnchantmentResponse)
def read_enchantment(item_id: int, roll_stat_id: int, db: Session = Depends(get_db)):
    try:
        enchantment = get_armory_enchantment(db, item_id, roll_stat_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not enchantment:
        raise HTTPException(status_code=404, detail="Enchantment not found")
    return enchantment


@router.get("/item/{item_id}", status_code=status.HTTP_200_OK, response_model=ArmoryEnchantmentResponse)
def read_item_enchantments(item_id: int, db: Session = Depends(get_db)):
    try:
        enchantments = get_armory_enchantments(db, item_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return enchantments



@router.delete("/item/{item_id}", status_code=status.HTTP_200_OK)
def delete_all_item_enchantments(item_id: int, db: Session = Depends(get_db)):
    try:
        deleted_count = remove_all_enchantments(db, item_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return {"deleted": deleted_count}


@router.delete("/{item_id}/{roll_stat_id}", status_code=status.HTTP_200_OK)
def delete_enchantment(item_id: int, roll_stat_id: int, db: Session = Depends(get_db)):
    try:
        enchantment = remove_enchantment(db, item_id, roll_stat_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not enchantment:
        raise HTTPException(status_code=404, detail="Enchantment not found")
    return enchantment
