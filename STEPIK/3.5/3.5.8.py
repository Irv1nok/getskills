from typing import Union


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money: Union['MoneyR', 'MoneyD', 'MoneyE']):
        money.cb = cls


class ValidateData:

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class MoneyR:
    cb = ValidateData()
    volume = ValidateData()

    def __init__(self, rub: Union[int, float] = 0) -> None:
        self.cb = None
        self.volume = rub
        self.wallet = 'rub'

    def __lt__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        res = other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub')
        return self.volume < round(res, 1)

    def __le__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        res = other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub')
        return self.volume <= round(res, 1)

    def __eq__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        res = other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub')
        return self.volume == round(res, 1)


class MoneyD:
    cb = ValidateData()
    volume = ValidateData()

    def __init__(self, dollar: Union[int, float] = 0) -> None:
        self.cb = None
        self.volume = dollar
        self.wallet = 'dollar'

    def __lt__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        volume_res = round(self.volume * self.cb.rates.get('rub'), 1)
        if not other.wallet == 'rub':
            other_res = round(other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub'), 1)
            return volume_res < other_res
        else:
            return volume_res < other.volume

    def __le__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        volume_res = round(self.volume * self.cb.rates.get('rub'), 1)
        if not other.wallet == 'rub':
            other_res = round(other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub'), 1)
            return volume_res <= other_res
        else:
            return volume_res <= other.volume

    def __eq__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        volume_res = round(self.volume * self.cb.rates.get('rub'), 1)
        if not other.wallet == 'rub':
            other_res = round(other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub'), 1)
            return volume_res == other_res
        else:
            return volume_res == other.volume


class MoneyE:
    cb = ValidateData()
    volume = ValidateData()

    def __init__(self, euro: Union[int, float] = 0) -> None:
        self.cb = None
        self.volume = euro
        self.wallet = 'euro'

    def __lt__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")


        volume_res = round(self.volume * self.cb.rates.get('rub') * self.cb.rates.get('euro'), 1)
        if not other.wallet == 'rub':
            other_res = round(other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub'), 1)
            return volume_res < other_res
        else:
            return volume_res < other.volume

    def __le__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        volume_res = round(self.volume * self.cb.rates.get('rub') * self.cb.rates.get('euro'), 1)
        if not other.wallet == 'rub':
            other_res = round(other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub'), 1)
            return volume_res <= other_res
        else:
            return volume_res <= other.volume

    def __eq__(self, other: Union['MoneyR', 'MoneyD', 'MoneyE']) -> bool:
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")

        volume_res = round(self.volume * self.cb.rates.get('rub') * self.cb.rates.get('euro'), 1)
        if not other.wallet == 'rub':
            other_res = round(other.volume * other.cb.rates.get(other.wallet) * other.cb.rates.get('rub'), 1)
            return volume_res == other_res
        else:
            return volume_res == other.volume

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)
eu = MoneyE(500)

CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(eu)


if r < d:
    print("неплохо")
else:
    print("нужно поднажать")
