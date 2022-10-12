class BookStudy:

    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author))

    def __eq__(self, other: "BookStudy") -> bool:
        return hash(self) == hash(other)

lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',]

lst_bs = set()
for lst in lst_in:
    name, author, year = lst.split(";")
    lst_bs.add(BookStudy(name, author, int(year)))
unique_books = len(lst_bs)
print(lst_bs)
print(unique_books)