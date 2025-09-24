from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from schemas.accessory import AccessoryCreate, AccessoryResponse
from database import get_db
from crud.accessory import create_accessory, get_accessory

router = APIRouter(prefix="/accessories", tags=["accessories"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_accessory(data: AccessoryCreate, db: Session = Depends(get_db)):
    try:
        accessory = create_accessory(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invalid Data: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return accessory


@router.get("/{accessory_id}", status_code=status.HTTP_200_OK, response_model=AccessoryResponse)
def read_accessory(accessory_id: int, db: Session = Depends(get_db)):
    try:
        accessory = get_accessory(db, accessory_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    if not accessory:
        raise HTTPException(status_code=404, detail="Accessory not found")
    return accessory
