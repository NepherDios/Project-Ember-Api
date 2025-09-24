from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from database import get_db
from schemas.inventory import (
    InventoryCreate,
    InventoryUpdate,
    InventoryResponse,
    InventoryItemWithDetails,
    InventoryWithDetailsResponse,
    InventoryWithCommonAttrResponse,
)
from crud.inventory import (
    add_item_to_inventory,
    update_inventory_slots,
    get_inventory,
    get_inventory_items_with_details,
    get_player_items,
    remove_from_inventory,
)

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_inventory_item(data: InventoryCreate, db: Session = Depends(get_db)):
    try:
        inv_row = add_item_to_inventory(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return inv_row


@router.put("/{player_id}", status_code=status.HTTP_200_OK, response_model=InventoryResponse)
def update_inventory(player_id: int, updated_data: InventoryUpdate, db: Session = Depends(get_db)):
    try:
        inv_rows = update_inventory_slots(db, player_id, updated_data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if inv_rows is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"items" : inv_rows}


@router.get("/{player_id}", status_code=status.HTTP_200_OK, response_model=InventoryResponse)
def read_inventory(player_id: int, db: Session = Depends(get_db)):
    try:
        inv_rows = get_inventory(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not inv_rows:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"items" : inv_rows}



@router.get("/items/{player_id}", response_model=InventoryWithDetailsResponse)
def read_player_items(player_id: int, db: Session = Depends(get_db)):
    try:
        items = get_player_items(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    if not items:
        raise HTTPException(status_code=404, detail="No items found")

    return {"items": items}



@router.get("/items/details/{player_id}", response_model=InventoryWithCommonAttrResponse)
def read_player_items_with_details(player_id: int, db: Session = Depends(get_db)):
    items = get_inventory_items_with_details(db, player_id)
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return {"items" : items}


@router.delete("/{player_id}/{slot_id}", status_code=status.HTTP_200_OK, response_model=InventoryItemWithDetails)
def delete_inventory_item(player_id: int, slot_id: int, db: Session = Depends(get_db)):
    try:
        inv_row = remove_from_inventory(db, player_id, slot_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not inv_row:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return inv_row
