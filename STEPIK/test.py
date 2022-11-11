# # # def __init__(self, rows: int, cols: int, **kwargs):
# # #     self.rows = rows
# # #     self.cols = cols
# # #     if 'cell' not in kwargs:
# # #         raise ValueError('параметр cell не указан')
# # #     self.cells = tuple(list(kwargs['cell']() for _ in range(cols)) for _ in range(rows))
# #
# # from math import isclose
# # # f"{type(self).__name__}
# # # """Дескриптор name"""
# # # self.name = f'_{owner.__name__}__{name}'
# # #
# # #
# # # i = 800.0005
# # # print(round(i, 1))
# #
# # import operator as op
# #
# #
# # class Vector:
# #     def __init__(self, *args):
# #         self.coords = args
# #
# #     def __len__(self):
# #         return len(self.coords)
# #
# #     def __do(self, other, f_name, new_object=True):
# #         if isinstance(other, self.__class__) and len(other) == len(self):
# #             new_coords = (f_name(a, b) for a, b in zip(self.coords, other.coords))
# #             print(new_coords)
# #         elif isinstance(other, (int, float)):
# #             new_coords = (f_name(b, other) for b in self.coords)
# #         else:
# #             raise ArithmeticError('размерности векторов не совпадают')
# #         if new_object:
# #             return self.__class__(*new_coords, )
# #         else:
# #             self.coords = (*new_coords,)
# #             return self
# #
# #     def __add__(self, other):
# #         return self.__do(other, op.add)
# #
# #     def __sub__(self, other):
# #         return self.__do(other, op.sub)
# #
# #     def __mul__(self, other):
# #         return self.__do(other, op.mul)
# #
# #     def __iadd__(self, other):
# #         return self.__do(other, op.add, False)
# #
# #     def __isub__(self, other):
# #         return self.__do(other, op.sub, False)
# #
# #     def __imul__(self, other):
# #         return self.__do(other, op.mul, False)
# #
# #     def __eq__(self, other):
# #         if isinstance(other, self.__class__):
# #             return self.coords == other.coords
# #         raise TypeError('Сравнение векторов не возможно!')
# #
# # v = Vector(1, 2, 3, 4, 5)
# #
# # v1 = Vector(1, 2, 3, 4, 5)
# #
# # v2 = v + v1
# # print(v2.__dict__)
# # v3 = v - v1
# # print(v3.__dict__)
# # print(v == v1)
# class Cell:
#     def __init__(self, value):
#         self.value = value
#
# class SparseTable:
#     def __init__(self):
#         self.tbl = {}
#
#     @property
#     def rows(self):
#         return max(i[0] for i in self.tbl) + 1 if self.tbl else 0
#
#     @property
#     def cols(self):
#         return max(i[1] for i in self.tbl) + 1 if self.tbl else 0
#
#     def add_data(self, row, col, data):
#         self.tbl[row, col] = data
#
#     def remove_data(self, row, col):
#         if not (row, col) in self.tbl:
#             raise IndexError('ячейка с указанными индексами не существует')
#         del self.tbl[row, col]
#
#     def __getitem__(self, key):
#         if not key in self.tbl:
#             raise ValueError('данные по указанным индексам отсутствуют')
#         return self.tbl[key].value
#
#     def __setitem__(self, key, v):
#         self.tbl.setdefault(key, Cell(0)).value = v
#
# st = SparseTable()
# st.add_data(2, 5, Cell("cell_25"))
# st.add_data(0, 0, Cell("cell_00"))
# st[2, 5] = 25 # изменение значения существующей ячейки
# st[11, 7] = 'cell_117' # создание новой ячейки
# print(st[0, 0]) # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице


x = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print(all([type(j) == int for i in x for j in i]))
