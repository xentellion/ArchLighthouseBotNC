import random


class StaticMethods:
    @staticmethod
    def amount():
        return f"{random.randint(100, 10000)}".lower()

    @staticmethod
    def mfr(data):
        if random.choice(data["type"]) == "самопал":
            manufacturer = "—"
        else:
            manufacturer = f'{random.choice(data["corporation"])}'
        return manufacturer.lower()

    @staticmethod
    def access(data):
        if random.choice(data["kind_accessory"]) == "имплант":
            acc = f'имплант (Защита: {random.choice(data["protection"])})'
        else:
            list = ["ручной", "нательный", "модуль к снаряжению"]
            acc = f"{random.choice(list)}"
        return acc.lower()

    @staticmethod
    def item(data):
        type_item = ["случайный", "имплант"]
        if random.choice(type_item) == "имплант":
            itm = f'имплант (защита:{random.choice(data["protection"])})'
        else:
            itm = f"случайный"
        return itm.lower()

    @staticmethod
    def m_amount(data):
        if random.choice(data["protection"]) == "есть":
            money = f"нет доступа (защищено)"
        else:
            money = f"{StaticMethods.amount()}"
        return money.lower()

    @staticmethod
    def number_id():
        num_idf = f"{random.randint(100000, 999999)}-{random.randint(100000, 999999)}-{random.randint(100000, 999999)}"
        return num_idf.lower()
