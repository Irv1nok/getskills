def __init__(self, rows: int, cols: int, **kwargs):
    self.rows = rows
    self.cols = cols
    if 'cell' not in kwargs:
        raise ValueError('параметр cell не указан')
    self.cells = tuple(list(kwargs['cell']() for _ in range(cols)) for _ in range(rows))

from math import isclose
# f"{type(self).__name__}
# """Дескриптор name"""
# self.name = f'_{owner.__name__}__{name}'
#
#
# i = 800.0005
# print(round(i, 1))

import operator as op


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __do(self, other, f_name, new_object=True):
        if isinstance(other, self.__class__) and len(other) == len(self):
            new_coords = (f_name(a, b) for a, b in zip(self.coords, other.coords))
            print(new_coords)
        elif isinstance(other, (int, float)):
            new_coords = (f_name(b, other) for b in self.coords)
        else:
            raise ArithmeticError('размерности векторов не совпадают')
        if new_object:
            return self.__class__(*new_coords, )
        else:
            self.coords = (*new_coords,)
            return self

    def __add__(self, other):
        return self.__do(other, op.add)

    def __sub__(self, other):
        return self.__do(other, op.sub)

    def __mul__(self, other):
        return self.__do(other, op.mul)

    def __iadd__(self, other):
        return self.__do(other, op.add, False)

    def __isub__(self, other):
        return self.__do(other, op.sub, False)

    def __imul__(self, other):
        return self.__do(other, op.mul, False)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.coords == other.coords
        raise TypeError('Сравнение векторов не возможно!')

v = Vector(1, 2, 3, 4, 5)

v1 = Vector(1, 2, 3, 4, 5)

v2 = v + v1
print(v2.__dict__)
v3 = v - v1
print(v3.__dict__)
print(v == v1)