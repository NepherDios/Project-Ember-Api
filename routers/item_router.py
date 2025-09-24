from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from database import get_db
from schemas.item import ItemCreate
from crud.item import (
    create_item,
    get_item,
)

router = APIRouter(prefix="/items", tags=["item"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_item(data: ItemCreate, db: Session = Depends(get_db)):
    try:
        new_item = create_item(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return new_item

@router.get("/{item_id}", status_code=status.HTTP_200_OK)
def read_item(item_id: int, db: Session = Depends(get_db)):
    try:
        item = get_item(db, item_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
