from typing import Any


class Cell:

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:

    def __init__(self, rows: int, cols: int, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.tabel = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def check_indx(self, key):
        r, c = key
        if type(r) != int or type(c) != int \
                or not (0 <= r < self.rows) \
                or not (0 <= c < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, key):
        self.check_indx(key)
        return self.tabel[key[0]][key[1]].data

    def __setitem__(self, key, value):
        self.check_indx(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.tabel[key[0]][key[1]].data = value

    def __iter__(self):
        for row in self.tabel:
            yield [x.data for x in row]


tb = TableValues(3, 2)
n = m = 0

for row in tb:
    n += 1
    print(row)
    for value in row:
        print(value)
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"
#
try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
