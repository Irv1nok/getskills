from random import choice
from string import ascii_letters, digits


class EmailValidator:

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email: str) -> bool:
        if EmailValidator.__is_email_str(email) and \
                all([True if chr in (ascii_letters + digits + '_.@)') else False for chr in email]):
            if email.count('@') == 1:
                name, address = email.split('@')
                if len(name) >= 100 or len(address) >= 50:
                    return False
                if name.count('..') > 0 or address.count('..') > 0 or address.count('.') == 0:
                    return False
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def get_random_email(cls) -> str:
        mail_name = (''.join(choice(ascii_letters + digits + '._') for i in range(10)))
        return f'{mail_name}@gmail.com'

    @staticmethod
    def __is_email_str(email: str) -> bool:
        return True if isinstance(email, str) else False


m = EmailValidator.get_random_email()
print(m)
print(EmailValidator.check_email(m))

res = EmailValidator.check_email("sc_lib@list.ru")
print(res)
# res = EmailValidator.check_email("sc_lib@list_ru")
