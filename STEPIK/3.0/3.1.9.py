from typing import Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        elif self.MIN_DIMENSION < value < self.MAX_DIMENSION:
            object.__setattr__(self, key, value)


# class Value:
#
#     def __set_name__(self, owner, name):
#         self.name = f'__{name}'
#
#     def __get__(self, instance, owner):
#         return property() if instance is None else getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if self.validate(value):
#             setattr(instance, self.name, value)
#
#     def validate(self, value) -> bool:
#         raise NotImplemented
#
#
# class Number(Value):
#     def validate(self, value) -> bool:
#         return isinstance(value, (int, float))
#
#
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#
#     a = Number()
#     b = Number()
#     c = Number()
#
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c
#
#     def __getattr__(self, item):
#         return False
#
#     def __setattr__(self, key, value):
#         if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
#             object.__setattr__(self, key, value)

d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError