from string import ascii_lowercase, digits


class CardCheck:

    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        x = number.split('-')
        if len(x) != 4:
            return False
        for i in x:
            if not i.isdigit() or len(i) != 4:
                return False
        return True

    @classmethod
    def check_name(cls, name: str) -> bool:
        name_and_surname = name.split()
        return all([x in cls.CHARS_FOR_NAME for n in name_and_surname for x in n]) and len(name_and_surname) == 2


# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(number):
#         """проверяет строку с номером карты и возвращает булево значение True,
#         если номер в верном формате и False - в противном случае. Формат номера,
#         следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)."""
#         figures = number.split('-')
#         return len(figures) == 4 and all([len(d) == 4 and d.isdigit() for d in figures])
#
#     @classmethod
#     def check_name(cls, name):
#         """проверяет строку name с именем пользователя карты.
#         Возвращает булево значение True, если имя записано верно
#         и False - в противном случае.
#         Формат имени: два слова (имя и фамилия) через пробел,
#         записанные заглавными латинскими символами и цифрами.
#         Например, SERGEI BALAKIREV."""
#         fi = name.split()
#         return all([c in cls.CHARS_FOR_NAME + ' ' for c in name]) and len(fi) == 2

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
print(is_number)
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name)