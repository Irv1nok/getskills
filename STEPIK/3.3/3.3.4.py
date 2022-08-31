class WordString:

    def __init__(self, string=''):
        self.__w_string = string

    def __len__(self):
        return len(self.string.split())

    @property
    def string(self):
        return self.__w_string

    @string.setter
    def string(self, set_str):
        self.__w_string = set_str

    def __call__(self, indx, *args, **kwargs):
        return self.__w_string.split()[indx]


words = WordString("1 2 3    4 5 6 7")
# words = WordString()
# words.string = "Курс  по Python   ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")