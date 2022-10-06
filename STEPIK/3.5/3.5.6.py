class Morph:

    def __init__(self, *args) -> None:
        self.words = list(args)

    def add_word(self, new_word: str) -> None:
        self.words.append(new_word)

    def get_words(self) -> tuple:
        return tuple(self.words)

    def __eq__(self, eq_word: str) -> bool:
        return True if eq_word.lower() in self.words else False


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]
text = input()
words = list(map(lambda x: x.strip("?!:;,.").lower(), text.split()))

count = 0
for obj in dict_words:
    for w in words:
        if w in obj.words:
            count += 1

print(count)
