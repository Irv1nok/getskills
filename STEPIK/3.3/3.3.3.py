class Model:

    def query(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        if len(self.__dict__) != 0:
            res = []
            for key, value in self.__dict__.items():
                res.append(f'{key} = {value}')
            return f'Model: {", ".join(res)}'
        return 'Model'

    def __len__(self):
        return len(self.__dict__)


m = Model()
m.query(id=10, fio='Сергей Балакирев', old=13)
print(m)
assert str(m).replace(' ', '') == "Model: id = 10, fio = Сергей Балакирев, old = 13".replace(' ', ''), "магический метод __str__ вернул неверные данные"
