class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            input_str = func(*args, **kwargs).split()
            return list(map(self.render, input_str))
        return wrapper


class RenderDigit:

    def __call__(self, res, *args, **kwargs):
        try:
            return int(res)
        except ValueError:
            return None


render = RenderDigit()
# d1 = render("123")   # 123 (целое число)
# print(d1)
# d2 = render("45.54")   # None (не целое число)
# print(d2)
# d3 = render("-56")   # -56 (целое число)
# print(d3)
# d4 = render("12fg")  # None (не целое число)
# print(d4)
# d5 = render("abc")   # None (не целое число)
# print(d5)
input_dg = InputValues(render)(input)
res = input_dg()
print(res)