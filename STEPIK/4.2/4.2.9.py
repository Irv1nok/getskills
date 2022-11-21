from typing import Tuple


class IteratorAttrs:

    def __iter__(self):
        yield from self.__dict__.items()


class SmartPhone(IteratorAttrs):

    def __init__(self, model: str, size: Tuple[int, int], memory: int):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('samsung', (1, 2), 3)
for attr, value in phone:
    print(attr, value)