from typing import Union
from math import sqrt

class Complex:

    def __init__(self, real: Union[int, float], img: Union[int, float]) -> None:
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if isinstance(value, (int, float)):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if isinstance(value, (int, float)):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.real ** 2 + self.img ** 2)


    """ЧЕРЕЗ ДЕСКРИПТОР ДАННЫХ"""
# class Des:
#     def __set_name__(self, owner, name):
#         self.name = f'_{owner.__name__}__{name}'
#
#     def __get__(self, instance, owner):
#         if instance:
#             return getattr(instance,self.name)
#
#     def __set__(self, instance, value):
#         if isinstance(value,(int,float)):
#             setattr(instance,self.name,value)
#         else:
#             raise ValueError("Неверный тип данных.")

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)

