#здесь объявляйте функцию-декоратор
def integer_params_decorated(func):
    def inner(self, *args, **kwargs):
        if not all([type(i) == int for i in args]):
            raise TypeError("аргументы должны быть целыми числами")
        if not all([type(i) == int for i in kwargs]):
            raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)
    return inner



def integer_params(cls):

    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():

        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        # print("init")
        self.__coords = list(args)

    def __getitem__(self, item):
        # print("getitem")
        return self.__coords[item]

    def __setitem__(self, key, value):
        # print("setitem")
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        # print("set_coords")
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
print("get_item >>", vector[1])
vector[1] = 20 # TypeError
# vector.set_coords(10, 11, 10.2)