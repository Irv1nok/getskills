from typing import Union


class Furniture:

    def __init__(self, name: str, weight: Union[int, float]):
        self._name = name
        self._weight = weight

    def __verify_name(self, value):
        if not isinstance(value, str):
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if weight <= 0 or type(weight) not in (int, float):
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, name, value):
        if name == "_name":
            self.__verify_name(value)
        elif name == "_weight":
            self.__verify_weight(value)

        object.__setattr__(self, name, value)

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):

    def __init__(self, name: str, weight: Union[int, float], tp: bool, doors: int):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):

    def __init__(self, name: str, weight: Union[int, float], height: Union[int, float]):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):

    def __init__(self, name: str, weight: Union[int, float], height: int, square: int):
        super().__init__(name, weight)
        self._height = height
        self._square = square

f = Furniture('12', 10)
cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)

print(tb.get_attrs())
