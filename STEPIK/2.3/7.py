class ValidateString:

    def __init__(self, min_length: int = 3, max_length: int = 100) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string: str) -> bool:
        return type(string) is str and self.min_length <= len(string) <= self.max_length

class StringValue:

    def __init__(self, validator=ValidateString()) -> None:
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login: str, password: str, email: str) -> None:
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self) -> list:
        return [self.login, self.password, self.email]

    def show(self) -> None:
        print('<form>\n'
              f'Логин:<{self.login}>\n'
              f'Пароль:<{self.password}>\n'
              f'Email:<{self.email}>\n'
              '</form>')


assert hasattr(ValidateString, 'validate'), "в классе ValidateString отсутствует метод validate"

r = RegisterForm('11111', '1111111', '11111111')
assert hasattr(r, 'login') and hasattr(r, 'password') and hasattr(r,
                                                                  'email'), "в классе RegisterForm должны быть дескрипторы login, password, email"

assert hasattr(RegisterForm, 'show'), "в классе RegisterForm отсутствует метод show"

StringValue.__doc__

frm = RegisterForm("123", "2345", "sc_lib@list.ru")
assert frm.get_fields() == ["123", "2345", "sc_lib@list.ru"], "метод get_fields вернул неверные данные"

frm.login = "root"
assert frm.login == "root", "дескриптор login вернул неверные данные"

v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world!") == False, "метод validate вернул неверное значение"


class A:
    st = StringValue(validator=ValidateString(3, 10))


a = A()
a.st = "hello"

assert a.st == "hello", "дескриптор StringValue вернул неверное значение"
a.st = "d"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной меньше min_length"
a.st = "dапарпаропропропропр"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной больше max_length"
a.st = "dапарпароп"
assert a.st == "dапарпароп", "дескриптор StringValue сохранил строку длиной больше max_length"
