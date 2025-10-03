import enum

class RarityType(str, enum.Enum):
    COMMON = "Common"
    MAGIC = "Magic"
    RARE = "Rare"
    LEGENDARY = "Legendary"
    