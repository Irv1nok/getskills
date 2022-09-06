from time import strftime
from time import gmtime


class DeltaClock:

    def __init__(self, clock1: "Clock", clock2: "Clock"):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        if self.__len__() < 0:
            return f'{strftime("%H: %M: %S", gmtime(0))}'
        return f'{strftime("%H: %M: %S", gmtime(self.__len__()))}'

    def __len__(self) -> int:
        diff_time = self.clock1.get_time() - self.clock2.get_time()
        if diff_time < 0:
            return 0
        return int(diff_time)


class Clock:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __setattr__(self, key, value):
        if value >= 0 and type(value) == int:
            return object.__setattr__(self, key, value)
        else:
            raise ValueError(f"Значение {key} меньше 0 или не целое число.")

    def get_time(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))  # 01: 30: 00
len_dt = len(dt)  # 5400
# print(str(dt))  #  возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)
# print(len_dt)  #  разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   #  отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
dt