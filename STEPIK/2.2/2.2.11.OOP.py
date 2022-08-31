class PhoneBook:
    BOOK = []

    @classmethod
    def add_phone(cls, phone: "PhoneNumber") -> None:
        cls.BOOK.append(phone)

    def remove_phone(cls, indx: int) -> None:
        cls.BOOK.pop(indx)

    @classmethod
    def get_phone_list(cls) -> list:
        return cls.BOOK


class PhoneNumber:

    def __init__(self, number: int, fio: str) -> None:
        self.number = number
        self.fio = fio




p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))

phones = p.get_phone_list()
print(phones)
