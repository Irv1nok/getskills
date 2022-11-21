from typing import Tuple


class Animal:

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old


class Cat(Animal):

    def __init__(self, name: str, old: int, color: str, weight: int):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):

    def __init__(self, name: str, old: int, breed: str, size: Tuple[int, int]):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


d = Dog('puzz', 2, 'tax', (2, 2))
print(d.get_info())
