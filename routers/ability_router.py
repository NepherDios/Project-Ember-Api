from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from database import get_db
from crud.ability import create_ability, update_ability, get_ability, get_player_abilities, remove_ability
from schemas import AbilityCreate, AbilityUpdate, AbilityResponse

router = APIRouter(prefix="/abilities", tags=["abilities"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def insert_ability(data: AbilityCreate, db: Session = Depends(get_db)):
    try:
        ability = create_ability(db, data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invalid Data: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    else:
        return ability


@router.get("/{ability_id}", status_code=status.HTTP_200_OK, response_model=AbilityResponse)
def read_ability(ability_id: int, db: Session = Depends(get_db)):
    try:
        ability = get_ability(db, ability_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    else:
        if not ability:
            raise HTTPException(status_code=404, detail="Ability Not Found")
        return ability


@router.get("/player/{player_id}", status_code=status.HTTP_200_OK, response_model=AbilityResponse)
def read_player_abilities(player_id: int, db: Session = Depends(get_db)):
    try:
        abilities = get_player_abilities(db, player_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    else:
        return abilities


@router.put("/{ability_id}", status_code=status.HTTP_200_OK)
def update_ability_data(ability_id: int, updated_data: AbilityUpdate, db: Session = Depends(get_db)):
    try:
        ability = update_ability(db, ability_id, updated_data)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invalid Update Data: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    else:
        if not ability:
            raise HTTPException(status_code=404, detail="Ability Not Found")
        return ability


@router.delete("/{ability_id}", status_code=status.HTTP_200_OK)
def delete_ability_data(ability_id: int, db: Session = Depends(get_db)):
    try:
        ability = remove_ability(db, ability_id)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Cannot delete ability due to constraint: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    else:
        if not ability:
            raise HTTPException(status_code=404, detail="Ability Not Found")
        return ability
