from typing import Union


class ItemAttrs:

    def __getitem__(self, index):
        key = list(self.__dict__.keys())[index]
        return self.__dict__[key]

    def __setitem__(self, index, value):
        key = list(self.__dict__.keys())[index]
        self.__dict__[key] = value


class Point(ItemAttrs):

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]
print(x)# 1
y = pt[1]
print(y)# 2.5
pt[0] = 10
print(pt.__dict__)