class DataBase:

    def __init__(self, path: str):
        self.path = path
        self.dict_db = {}

    def write(self, record: "Record"):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk: "Record"):
        res = [obj for r in self.dict_db.values() for obj in r if obj.pk == pk]
        return res[0]


class Record:
    KEY_ID = 1

    def __init__(self, fio: str, descr: str, old: int):
        self.pk = self.KEY_ID
        self.fio = fio
        self.descr = descr
        self.old = old
        Record.KEY_ID += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: "Record"):
        return hash(self) == hash(other)


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33']

db = DataBase("data")
for s in lst_in:
    fio, descr, old = s.split(";")
    db.write(Record(fio, descr, int(old)))

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)

assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"