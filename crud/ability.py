from models.ability import Ability
from schemas.ability import AbilityCreate, AbilityUpdate
from sqlalchemy.orm import Session

#Creates an ability when the player is created or gets a new skill
#Or recreates the ability if the player resets the skill tree(If implemented)
def create_ability(session: Session, data: AbilityCreate) -> Ability:
    ability = Ability(**data.dict())
    
    session.add(ability)
    session.commit()
    session.refresh(ability)
    
    return ability

#Updates either the skill key, the skill slot or both depending on the updated_data
def update_ability(session: Session, ability_id: int, updated_data: AbilityUpdate) -> Ability | None:
    ability = session.query(Ability).filter(Ability.ability_id == ability_id).first()
    
    if not ability:
        return None
    
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(ability, key, value)
    
    session.commit()
    session.refresh(ability)
    
    return ability
    
#Gets one ability by it's id
def get_ability(session: Session, ability_id: int) -> Ability | None:
    return session.query(Ability).filter(Ability.ability_id == ability_id).first()

#Gets all player abilities by player_id
def get_player_abilities(session: Session, player_id: int) -> list[Ability] | None:
    return session.query(Ability).filter(Ability.player_id == player_id).all()

#Either Deletes or removes the ability from the player
#It depends wether removed by admin or reseted by player form skill tree tho code doesn't change :P
def remove_ability(session: Session, ability_id: int) -> Ability | None:
    ability = session.query(Ability).filter(Ability.ability_id == ability_id).first()
    
    if ability:
        session.delete(ability)
        session.commit()
    
    return ability