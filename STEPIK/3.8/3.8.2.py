class Record:

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __getitem__(self, item: str) -> str:
        if not isinstance(item, int) or not 0 <= item <= (len(self.__dict__) - 1):
            raise IndexError('неверный индекс поля')
        indx = list(self.__dict__)[item]
        return self.__dict__[indx]

    def __setitem__(self, key: str, value: str) -> None:
        if not isinstance(key, int) or key < 0:
            raise IndexError('неверный индекс поля')
        indx = list(self.__dict__)[key]
        self.__dict__[indx] = value

r = Record(pk=1, title='Python ООП', author='Балакирев')
