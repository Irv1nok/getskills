class Car:

    def __init__(self):
        self.__model = str

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, n: str):
        if isinstance(n, str) and 2 < len(n) < 100:
            self.__model = n

car = Car()
car.model = 'Toyota'
print(car)