from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from schemas.general_item import GeneralItemCreate, GeneralItemResponse
from database import get_db
from crud.general_item import create_general_item, get_general_item

router = APIRouter(prefix="/general_items", tags=["general_items"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_general_item(data: GeneralItemCreate, db: Session = Depends(get_db)):
    try:
        general_item = create_general_item(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invalid Data: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return general_item


@router.get("/{general_item_id}", status_code=status.HTTP_200_OK, response_model=GeneralItemResponse)
def read_general_item(general_item_id: int, db: Session = Depends(get_db)):
    try:
        general_item = get_general_item(db, general_item_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not general_item:
        raise HTTPException(status_code=404, detail="General item not found")
    return general_item
