from math import sqrt


class LineTo:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args) -> None:
        self.lines = [LineTo(0, 0)]
        self.lines.extend(args)

    def get_path(self) -> list:
        return self.lines

    def get_length(self) -> float:
        data_x_y = []
        for obj in self.lines:
            data_x_y.append([obj.x, obj.y])

        sum_dist = 0
        for i in range(len(data_x_y) - 1):
            sum_dist += sqrt((data_x_y[i + 1][0] - data_x_y[i][0]) ** 2 + (data_x_y[i + 1][1] - data_x_y[i][1]) ** 2)
        return sum_dist

    def add_line(self, line: "lineTo") -> None:
        self.lines.append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
# print(p.get_path())

# class LineTo:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def length(self, x1, y2):
#         return ((self.x - x1) ** 2 + (self.y - y2) ** 2) ** 0.5
#
#
# class PathLines:
#
#     def __init__(self, *points):
#         self.__points = list(points)
#
#     def add_line(self, point):
#         self.__points.append(point)
#
#     def get_path(self):
#         return self.__points
#
#     def get_length(self):
#         x = y = length = 0
#         for point in self.__points:
#             length += point.length(x, y)
#             x, y = point.x, point.y
#         return length
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print(dist)
