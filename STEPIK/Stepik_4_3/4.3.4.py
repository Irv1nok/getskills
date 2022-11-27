from typing import Tuple


class Thing:

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):

    def __init__(self, name: str, weight: float, author: str, date: str):
        super().__init__(name, weight)
        self.author = author
        self.date = date

class Computer(Thing):

    def __init__(self, name: str, weight: float, memory: int, cpu: str):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu

class Auto(Thing):

    def __init__(self, name: str, weight: float, dims: Tuple[int, float]):
        super().__init__(name, weight)
        self.dims = dims

class Mercedes(Auto):

    def __init__(self, name: str, weight: float, dims: Tuple[int, float], model: str, old: int):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old

class Toyota(Auto):

    def __init__(self, name: str, weight: float, dims: Tuple[int, float], model: str, wheel: bool):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

