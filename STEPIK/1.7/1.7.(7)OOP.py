from string import ascii_lowercase, digits

    # здесь объявляйте классы TextInput и PasswordInput
class TextInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class="login">{self.name}:<input type="text" size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if not 3 <= len(name) <= 50 and all([n in cls.CHARS_CORRECT for n in name]):
            raise ValueError("некорректное поле name")

class PasswordInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class="password">{self.name}:<input type="text" size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if not 3 <= len(name) <= 50 and all([n in cls.CHARS_CORRECT for n in name]):
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

    # эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()