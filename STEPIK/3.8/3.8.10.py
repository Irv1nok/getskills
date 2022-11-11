class SparseTable:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = {}

    def calc_row_cols(self):
        self.rows = max(key[0] for key in self.data) + 1
        self.cols = max(key[1] for key in self.data) + 1

    def add_data(self, row, col, data):
        self.data[(row, col)] = data
        self.calc_row_cols()

    def remove_data(self, row, col):
        try:
            del self.data[(row, col)]
        except KeyError:
            raise IndexError

        self.calc_row_cols()

    def __getitem__(self, item):
        try:
            return self.data[item].value
        except KeyError:
            raise ValueError

    def __setitem__(self, key, value):

        if not self.data.get(key):
            self.data[key] = Cell(value)
            self.calc_row_cols()
        else:
            self.data[key] = Cell(value)


class Cell:

    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице