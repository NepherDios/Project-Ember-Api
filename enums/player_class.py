import enum

class PlayerClass(str, enum.Enum):
    MAGE = "Mage"
    RANGER = "Ranger"
    WARRIOR = "Warrior"