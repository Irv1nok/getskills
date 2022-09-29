class StringText:

    def __init__(self, lst_words: list) -> None:
        self.lst_words = lst_words

    def __str__(self):
        print(self.lst_words)
        return ' '.join(self.lst_words)

    def __len__(self) -> int:
        s = self.lst_words[0].split(' ')
        return len(s)

    def __lt__(self, other: "StringText") -> bool:
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other: "StringText") -> bool:
        return len(self.lst_words) <= len(other.lst_words)

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


lst_words = [[string.strip('–?!,.;')] for string in stich]
lst_text = [StringText(x) for x in lst_words]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [str(x) for x in lst_text_sorted]
print(lst_text_sorted)
