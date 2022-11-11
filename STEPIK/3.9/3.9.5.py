from typing import Union


class Person:

    def __init__(self, fio: str, job: str, old: int, salary: Union[int, float], year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.attrs = tuple(self.__dict__)

    @staticmethod
    def check_idx(i):
        if not 0 <= i <= 4:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        if self.count < 4:
            self.count += 1
            return list(self.__dict__.values())[self.count]
        else:
            del self.count
            raise StopIteration

    def __getitem__(self, item):
        self.check_idx(item)
        return getattr(self, self.attrs[item])

    def __setitem__(self, key, value):
        self.check_idx(key)
        setattr(self, self.attrs[key], value)

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# print(pers.__dict__)
pers[0] = 'Балакирев С.М.'
# print(pers.__dict__)
for v in pers:
    print(v)


