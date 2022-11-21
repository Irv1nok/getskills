from typing import Union, Any
from functools import wraps
import operator as op


def check_dimension(func):
    @wraps(func)
    def wrapper(obj, other):
        if not len(obj.vector_coords) == len(other.vector_coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return func(obj, other)

    return wrapper


class Vector:

    def __init__(self, *args: Union[int, float]):
        self.vector_coords = list(args)

    def get_coords(self):
        return tuple(self.vector_coords)

    def execute_arithmetic_func(self, other, func_operator):
        if isinstance(other, self.__class__):
            new_obj = VectorInt(*map(func_operator, self.vector_coords, other.vector_coords))

        elif type(other) is Vector or type(self) is Vector:
            new_obj = Vector(*map(func_operator, self.vector_coords, other.vector_coords))

        return new_obj

    @check_dimension
    def __add__(self, other: Any["Vector", "VectorInt"]) -> Any["Vector", "VectorInt"]:
        return self.execute_arithmetic_func(other, op.add)

    @check_dimension
    def __sub__(self, other: Any["Vector", "VectorInt"]) -> Any["Vector", "VectorInt"]:
        return self.execute_arithmetic_func(other, op.sub)


class VectorInt(Vector):

    def __init__(self, *args: int):
        if any(map(lambda x: type(x) != int, args)):
            raise ValueError('координаты должны быть целыми числами')
        self.vector_coords = list(args)








v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"