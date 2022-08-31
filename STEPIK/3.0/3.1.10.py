import time


class Validate:

    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not hasattr(instance, 'date'):
            return setattr(instance, self.name, value)


class Mechanical:
    date = Validate()

    def __init__(self, date: float):
        self.date = date


class Aragon:
    date = Validate()

    def __init__(self, date: float):
        self.date = date


class Calcium:
    date = Validate()

    def __init__(self, date: float):
        self.date = date


class GeyserClassic:
    MAX_DATE_FILTER = 100
    ALLIGN_FILTER = {'1': Mechanical, '2': Aragon, '3': Calcium}

    def __init__(self):
        self.slot_1 = 0
        self.slot_2 = 0
        self.slot_3 = 0

    def add_filter(self, slot_num, filter):
        if self.ALLIGN_FILTER[str(slot_num)] == type(filter):
            if slot_num == 1 and not self.slot_1:
                self.slot_1 = filter
            elif slot_num == 2 and not self.slot_2:
                self.slot_2 = filter
            elif slot_num == 3 and not self.slot_3:
                self.slot_3 = filter

    def remove_filter(self, slot_num):
        setattr(self, f'slot_{slot_num}', 0)

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        if all([self.slot_1, self.slot_2, self.slot_3]):
            for obj in self.get_filters():
                if 0 <= time.time() - obj.date <= self.MAX_DATE_FILTER:
                    pass
                else:
                    return False
            return True
        return False


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3,
                                                                            Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
