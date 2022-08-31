class Model:
    def __init__(self):
        self.model = 'Model'

    def query(self, **kwargs):
        self.model += ': ' + ', '.join(map(lambda i: f'{i[0]} = {i[1]}', kwargs.items()))

    def __str__(self):
        return self.model


m = Model()
m.query(id=10, fio='Сергей Балакирев', old=13)
print(m)
assert str(m).replace(' ', '') == "Model: id = 10, fio = Сергей Балакирев, old = 13".replace(' ', ''), "магический метод __str__ вернул неверные данные"