import sys

# здесь пишите программу
class Book:

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'

lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка из входного потока (эту строчку не менять)
title, author, pages = lst_in
b = Book(title, author, pages)
print(b)