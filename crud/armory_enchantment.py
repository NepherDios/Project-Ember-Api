from models.armory_enchantment import ArmoryEnchantment
from schemas.armory_enchantment import ArmoryEnchantmentCreate, ArmoryEnchantmentUpdate
from sqlalchemy.orm import Session

def create_armory_enchantment(session: Session, data: ArmoryEnchantmentCreate) -> ArmoryEnchantment:
    armory_enchantment = ArmoryEnchantment(**data.dict())
    
    session.add(armory_enchantment)
    session.commit()
    session.refresh(armory_enchantment)
    
    return armory_enchantment


def update_armory_enchantment(session: Session, item_id: int, roll_stat_id: int, updated_data: ArmoryEnchantmentUpdate) -> ArmoryEnchantment | None:
    armory_enchantment = session.query(ArmoryEnchantment).filter(ArmoryEnchantment.item_id == item_id, ArmoryEnchantment.roll_stat_id == roll_stat_id).first()
    
    if not armory_enchantment:
        return None
    
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(armory_enchantment, key, value)
        
    session.commit()
    session.refresh(armory_enchantment)
    
    return armory_enchantment


def get_armory_enchantment(session: Session, item_id: int, roll_stat_id: int) -> ArmoryEnchantment | None:
    return session.query(ArmoryEnchantment).filter(ArmoryEnchantment.item_id == item_id, ArmoryEnchantment.roll_stat_id == roll_stat_id).first()


def get_armory_enchantments(session: Session, item_id: int) -> list[ArmoryEnchantment] | None:
    return session.query(ArmoryEnchantment).filter(ArmoryEnchantment.item_id == item_id).all()


def remove_enchantment(session: Session, item_id: int, roll_stat_id: int) -> ArmoryEnchantment | None:
    enchantment = session.query(ArmoryEnchantment).filter(ArmoryEnchantment.item_id == item_id, ArmoryEnchantment.roll_stat_id == roll_stat_id).first()
    
    if enchantment:
        session.delete(enchantment)
        session.commit()
        
    return enchantment


def remove_all_enchantments(session: Session, item_id: int) -> int:
    enchantments_removed = session.query(ArmoryEnchantment).filter(ArmoryEnchantment.item_id == item_id).delete(synchronize_session=False)
    session.commit()
    
    return enchantments_removed