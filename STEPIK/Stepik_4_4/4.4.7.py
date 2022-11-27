class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


class TemperatureView(Observer):
    def update(self, obj: "Data"):
        print(f"Текущая температура {obj.temp}")



class PressureView(Observer):
    def update(self, obj: "Data"):
        print(f"Текущее давление {obj.press}")


class WetView(Observer):
    def update(self, obj: "Data"):
        print(f"Текущая влажность {obj.wet}")
