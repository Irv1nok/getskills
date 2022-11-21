class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        if not self._is_valid(*args):
            raise ValueError('данные не прошли валидацию')
        return True


class IntegerValidator(Validator):

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) == int and self.min_value <= data <= self.max_value


class FloatValidator(Validator):

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: float):
        return type(data) == float and self.min_value <= data <= self.max_value


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError