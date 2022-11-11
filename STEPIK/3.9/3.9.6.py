class TriangleListIterator:

    def __init__(self, lst: list):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]


ls = [['1'], [2, 3], [4, 5, 6], ['7', 8, '9', 10]]
ls_one = [x for row in ls for x in row]

t = TriangleListIterator(ls)
for i, x in enumerate(t):
    print(x)
assert x == ls_one[i], "итератор вернул неверное значение"

# lst = [["x00"],
#        ["x10", "x11"],
#        ["x20", "x21", "x22"],
#        ["x30", "x31", "x32", "x33"]
#        ]

# it = TriangleListIterator(lst)
# it_iter = iter(it)
#
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
# print(next(it_iter))
