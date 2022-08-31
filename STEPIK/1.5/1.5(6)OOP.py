class TriangleChecker:

    def __init__(self, a, b, c):
        self.coord = [a, b, c]

    def is_triangle(self):
        if all([isinstance(v, int) for v in self.coord]) is False or all([v > 0 for v in self.coord]) is False:
            return 1
        self.coord.sort()
        if self.coord[0] + self.coord[1] <= self.coord[2]:
            return 2
        return 3

a, b, c = [10, 5, 3]
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


# class TriangleChecker:
#     def __init__(self, a: int, b: int, c: int):
#         self.s = [a, b, c]
#
#     def is_triangle(self) -> (1, 2, 3):
#         if max(self.s) * 2 < sum(self.s):
#             return 1
#         if min(self.s) <= 0:
#             return 2
#         return 3
#
#
# a, b, c = map(int, input().split())  # эту строчку не менять
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())