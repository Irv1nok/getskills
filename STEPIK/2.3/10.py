class TVProgram:

    def __init__(self, name: str) -> None:
        self.name = name
        self.items = []

    def add_telecast(self, tl: 'Telecast') -> None:
        self.items.append(tl)

    def remove_telecast(self, id: int) -> None:
        tl_obj = [obj for obj in self.items if obj.uid == id]
        self.items.remove(*tl_obj)


class Telecast:

    def __init__(self, id: int, name: str, duration: int) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, dur):
        self.__duration = dur

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(2)
for t in pr.items:
    print(f"{t.name}: {t.duration}")