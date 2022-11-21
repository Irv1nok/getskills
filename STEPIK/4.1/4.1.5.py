from typing import Tuple


class Thing:
    ID_COUNT = 0

    def __init__(self, name: str, price: float):
        self.id = self.id_count()
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    @classmethod
    def id_count(cls):
        Thing.ID_COUNT += 1
        return Thing.ID_COUNT

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):

    def __init__(self, name: str, price: float, weight: float, dims: Tuple[float, float, float]):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):

    def __init__(self, name: str, price: float, memory: int, frm: str):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

th = Thing('value', 22)

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())