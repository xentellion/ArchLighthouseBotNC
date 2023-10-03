from enum import Enum


class Races(Enum):
    HUMAN = "человек"
    HARPY = "гарпия"
    SATYR = "сатир"
    TYPHON = "тифон"
    WYVERN = "виверна"
    TELHIN = "тельхин"


class Loot(Enum):
    WEAPON = "оружие"
    ARMOR = "основная броня"
    EXTRA_ARMOR = "дополнительная броня"
    EQUIPMENT = "вспомогательное снаряжение"
    ACCESSORY = "аксессуар"
    CONSUMABLE = "расходник"
    DEVICE = "устройство"
    GENERIC = "повседневный предмет"
    RARE = "ценный предмет"
    MONEY = "деньги"

