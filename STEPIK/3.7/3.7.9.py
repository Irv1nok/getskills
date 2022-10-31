from typing import Union
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

    def execute_arithmetic_func(self, other, func_operator, new_class_obj=True):
        if isinstance(other, self.__class__):
            new_obj = Vector(*map(func_operator, self.vector_coords, other.vector_coords))

        elif type(other) in (int, float):
            self.vector_coords = [func_operator(coord, other) for coord in self.vector_coords]

        if new_class_obj:
            return new_obj
        return self

    @check_dimension
    def __add__(self, other: "Vector") -> "Vector":
        return self.execute_arithmetic_func(other, op.add)

    #
    @check_dimension
    def __sub__(self, other: "Vector") -> "Vector":
        return self.execute_arithmetic_func(other, op.sub)

    #
    @check_dimension
    def __mul__(self, other: "Vector") -> "Vector":
        return self.execute_arithmetic_func(other, op.mul)

    #
    def __iadd__(self, other: Union["Vector", int]) -> "Vector":
        return self.execute_arithmetic_func(other, op.iadd, False)

    def __isub__(self, other) -> "Vector":
        return self.execute_arithmetic_func(other, op.isub, False)

    def __eq__(self, other: "Vector") -> bool:
        return self.vector_coords == other.vector_coords


v = Vector(1, 2, 3, 4, 5)

v1 = Vector(1, 2, 3, 4, 5)

v += v1
v -= v1
print(v.__dict__)
