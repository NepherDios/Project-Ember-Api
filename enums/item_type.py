import enum

class ItemType(str, enum.Enum):
    GENERAL_ITEM = "GeneralItem"
    WEAPON = "Weapon"
    ARMOR = "Armor"
    ACCESSORY = "Accessory"
