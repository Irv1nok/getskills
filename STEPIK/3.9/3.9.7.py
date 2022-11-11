class IterColumn:

    def __init__(self, lst: list, column: int):
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.iter_lst = [x[self.column] for x in self.lst]
        self.indx = -1
        return self

    def __next__(self):
        self.indx += 1
        if self.indx < len(self.iter_lst):
            return self.iter_lst[self.indx]
        else:
            raise StopIteration

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]


it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)
#
# it_iter = iter(it)
#
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))