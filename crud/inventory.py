from models.inventory import Inventory
from schemas.inventory import InventoryCreate, InventoryUpdate, InventoryItemWithCommonAttr, ItemDetails, InventoryItemWithDetails
from schemas.item import ItemDetailsWithCommonAttr
from schemas.equipment_common_attr import EquipmentCommonAttrResponse
from models.item import ItemType
from sqlalchemy.orm import Session

#Adds an item to the inventory after common_attr -> item -> weapon/armor/accessory/general_item have been created and it's slot_id defined
def add_item_to_inventory(session: Session, data: InventoryCreate) -> Inventory:
    inv_row = Inventory(**data.model_dump())
    
    session.add(inv_row)
    session.commit()
    session.refresh(inv_row)
    
    return inv_row

#updates the inventory once a change has been made
def update_inventory_slots(session: Session, player_id: int, updated_data: InventoryUpdate) -> list[Inventory] | None:
    inv_rows = session.query(Inventory).filter(Inventory.player_id == player_id).all()
    
    if not inv_rows:
        return None
    
    for slot_id, new_item_id in updated_data.model_dump(exclude_unset=True).items():
        for inv_row in inv_rows:
            if inv_row.slot_id == slot_id:
                inv_row.item_id = new_item_id
                break
        
    session.commit()
    
    return inv_rows
    
#Gets only information like player_id, slot_id and item_id
def get_inventory(session: Session, player_id: int) -> list[Inventory] | None:
    return session.query(Inventory).filter(Inventory.player_id == player_id).all()

#Gets the actual inventory items objects in a list
def get_player_items(session: Session, player_id: int) -> list[InventoryItemWithDetails]:
    inventory_rows = get_inventory(session, player_id)
    detailed_items = []

    for inv in inventory_rows:
        if not inv.item:
            continue

        item = inv.item
        detailed_items.append(
            InventoryItemWithDetails(
                slot_id=inv.slot_id,
                item=ItemDetails(
                    item_id=item.item_id,
                    item_name=getattr(item, "item_name", None),
                    item_type=item.item_type,
                )
            )
        )

    return detailed_items



def get_inventory_items_with_details(session: Session, player_id: int):
    inventory_rows = session.query(Inventory).filter(Inventory.player_id == player_id).all()
    detailed_items = []

    for inv in inventory_rows:
        item = inv.item
        if not item:
            continue

        if item.equipment_common_attr:
            common_attr = EquipmentCommonAttrResponse.model_validate(item.equipment_common_attr)
        else:
            common_attr = None

        detailed_item = ItemDetailsWithCommonAttr(
            item_id=item.item_id,
            item_name=getattr(item, "item_name", None),
            item_type=item.item_type,
            common_attr=common_attr,
        )

        detailed_items.append(
            InventoryItemWithCommonAttr(
                slot_id=inv.slot_id,
                item=detailed_item,
            )
        )

    return detailed_items


#Removes an item from the inventory
def remove_from_inventory(session: Session, player_id: int, slot_id: int) -> Inventory | None:
    inv = session.query(Inventory).filter(Inventory.player_id == player_id, Inventory.slot_id == slot_id).first()
    
    if inv:
        session.delete(inv)
        session.commit()
        
    return inv