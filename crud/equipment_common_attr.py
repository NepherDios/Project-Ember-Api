from models.equipment_common_attr import EquipmentCommonAttr
from schemas.equipment_common_attr import EquipmentCommonAttrCreate, EquipmentCommonAttrUpdate
from sqlalchemy.orm import Session

def create_equipment_common_attr(session: Session, data: EquipmentCommonAttrCreate) -> EquipmentCommonAttr:
    common_attr = EquipmentCommonAttr(**data.model_dump())
    session.add(common_attr)
    session.commit()
    session.refresh(common_attr)
    return common_attr

def get_equipment_common_attr(session: Session, common_attr_id: int) -> EquipmentCommonAttr | None:
    return session.query(EquipmentCommonAttr).filter(EquipmentCommonAttr.common_attr_id == common_attr_id).first()

def update_equipment_common_attr(session: Session, common_attr_id: int, updated_data: EquipmentCommonAttrUpdate) -> EquipmentCommonAttr | None:
    common_attr = get_equipment_common_attr(session, common_attr_id)
    if not common_attr:
        return None
    
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(common_attr, key, value)
    
    session.commit()
    session.refresh(common_attr)
    return common_attr

def delete_equipment_common_attr(session: Session, common_attr_id: int) -> EquipmentCommonAttr | None:
    common_attr = get_equipment_common_attr(session, common_attr_id)
    if common_attr:
        session.delete(common_attr)
        session.commit()
    return common_attr
