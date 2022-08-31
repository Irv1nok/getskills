class FloatValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) is float:
            setattr(instance, self.name, value)
        else:
            raise TypeError('Присваивать можно только вещественный тип данных.')


class Cell:
    value = FloatValue()

    def __init__(self, value: float = 0.0) -> None:
        self.value = value


class TableSheet:

    def __init__(self, n: int, m: int) -> None:
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]



table = TableSheet(5, 3)

i = 1.0
for n in range(5):
    for m in range(3):
        table.cells[n][m].value = i
        i += 1.0

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
print(res)
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
