import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for field in data:
            self.lst_data.append(dict(zip(self.FIELDS, field.split())))

    def select(self, a, b):
        return self.lst_data[a:b+1]





db = DataBase()
db.insert(['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200'])
print(db.lst_data)
print(db.select(1, 2))

