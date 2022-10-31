class Integer:

    def __init__(self, start_value: int = 0):
        self.__value = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, val: int):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)


class Array:

    def __init__(self, max_length: int, cell: "Integer"):
        self.max_length = max_length
        self.cell = cell
        self.lst_array = [self.cell() for _ in range(self.max_length)]

    def chk_index(self, i: int):
        if type(i) != int or i < 0 or i >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item: int) -> "Integer":
        self.chk_index(item)
        return self.lst_array[item].value

    def __setitem__(self, key: int, value):
        self.chk_index(key)
        self.lst_array[key].value = value

    def __str__(self):
        return " ".join(map(str, self.lst_array))


ar_int = Array(10, cell=Integer)

print(ar_int[3])
print(ar_int[1])
ar_int[1] = 10

print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
