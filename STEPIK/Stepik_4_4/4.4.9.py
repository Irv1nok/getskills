# здесь объявляйте декоратор и все что с ним связано


def class_log(vector_log):
    def log_methods(self):
        # print("log_self", self)
        methods = {k: v for k, v in self.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(self, k, decorated_function_cls(v))
        return self

    def decorated_function_cls(func):
        # print("decor_func", func)
        def wrapper(*args, **kwargs):
            # print("wrap_args", args, kwargs)
            vector_log.append(func.__name__)
            # print("dec_wr_ret")
            return func(*args, **kwargs)
        return wrapper
    return log_methods

vector_log: list = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)

v[0] = 10
print(vector_log)
