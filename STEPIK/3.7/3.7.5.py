class MailBox:

    def __init__(self):
        self.inbox_list = []

    def receive(self, lst):
        self.inbox_list = [MailItem(*l.split('; ')) for l in lst]


class MailItem:

    def __init__(self, mail_from: str, title: str, content: str):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read if fl_read else False

    def __bool__(self) -> bool:
        return self.is_read



lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']

mail = MailBox()
mail.receive(lst_in)
print(mail.inbox_list)
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(inbox_list_filtered)