from typing import Union


class SellItem:

    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class House(SellItem):

    def __init__(self, name: str, price: Union[int, float], material: str, square: Union[int, float]):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):

    def __init__(self, name: str, price: Union[int, float], size: Union[int, float], rooms: int):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):

    def __init__(self, name: str, price: Union[int, float], square: Union[int, float]):
        super().__init__(name, price)
        self.square = square


class Agency:

    def __init__(self, name: str):
        self.name = name
        self.list_obj: list = []

    def add_object(self, obj):
        self.list_obj.append(obj)

    def remove_object(self, obj):
        self.list_obj.remove(obj)

    def get_objects(self):
        return self.list_obj


ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)]  # выделение списка домов
