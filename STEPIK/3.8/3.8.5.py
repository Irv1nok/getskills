class DescriptorValue:

    def __init__(self, init_type):
        self.init_type = init_type

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != self.init_type:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:

    value = DescriptorValue(int)

    def __init__(self, start_value: int = 0):
        self.value = start_value

    def __repr__(self):
        return str(self.value)


class CellString:

    value = DescriptorValue(str)

    def __init__(self, start_value: str = ''):
        self.value = start_value

    def __repr__(self):
        return str(self.value)


class TableValues:

    def __init__(self, rows: int, cols: int, **kwargs):
        self.rows = rows
        self.cols = cols
        if 'cell' not in kwargs:
            raise ValueError('параметр cell не указан')
        self.cells = tuple(list(kwargs['cell']() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, item):
        i, j = item
        return self.cells[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        self.cells[i][j].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
print(table.cells)
# tb = TableValues(3, 2, cell=CellInteger)
# tb[0, 0] = 1
# assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"
#
# try:
#     tb[2, 1] = 1.5
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# for row in tb.cells:
#     for x in row:
#         assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"
#
# cell = CellInteger(10)
# assert cell.value == 10, "дескриптор value вернул неверное значение"