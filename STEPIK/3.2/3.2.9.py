class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        res = self.func().strip('"').split(' ')
        return list(map(int, res))


input_dg = InputDigits(input)

res = input_dg()
