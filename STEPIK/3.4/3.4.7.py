from typing import Union


class Book:

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title if type(title) == str else ""
        self.author = author if type(author) == str else ""
        self.year = year if type(year) == int else None


class Lib:

    def __init__(self) -> None:
        self.book_list = []

    def __add__(self, other: "Book") -> "Self":
        self.book_list.append(other)
        return self

    def __sub__(self, other: Union[Book, int]) -> None:
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif type(other) == int:
            self.book_list.pop(other)
        return self

    def __len__(self) -> len:
        return len(self.book_list)
