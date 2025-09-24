from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from database import get_db
from schemas.equipment_common_attr import EquipmentCommonAttrCreate, EquipmentCommonAttrResponse
from crud.equipment_common_attr import create_equipment_common_attr, get_equipment_common_attr, delete_equipment_common_attr

router = APIRouter(prefix="/equipment_common_attr", tags=["equipment_common_attr"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_equipment_common_attr(data: EquipmentCommonAttrCreate, db: Session = Depends(get_db)):
    try:
        common_attr = create_equipment_common_attr(db, data)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return common_attr


@router.get("/{common_attr_id}", status_code=status.HTTP_200_OK, response_model=EquipmentCommonAttrResponse)
def read_equipment_common_attr(common_attr_id: int, db: Session = Depends(get_db)):
    try:
        common_attr = get_equipment_common_attr(db, common_attr_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not common_attr:
        raise HTTPException(status_code=404, detail="Equipment common attribute not found")
    return common_attr

@router.delete("/{common_attr_id}", status_code=status.HTTP_200_OK)
def delete_equipment_common_attr_route(common_attr_id: int, db: Session = Depends(get_db)):
    try:
        common_attr = get_equipment_common_attr(db, common_attr_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    if not common_attr:
        raise HTTPException(status_code=404, detail="Equipment common attribute not found")
    else:
        delete_equipment_common_attr(db, common_attr_id)
        return {"detail": f"Equipment common attribute {common_attr_id} deleted successfully"}

    