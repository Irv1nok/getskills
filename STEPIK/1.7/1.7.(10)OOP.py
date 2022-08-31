class Viber:
    msg_pool = {}

    @classmethod
    def add_message(cls, msg):
        cls.msg_pool[msg] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msg_pool.pop(msg)

    @classmethod
    def set_like(cls, msg):
        cls.msg_pool[msg].fl_like = not cls.msg_pool[msg].fl_like
        # True if cls.msg_pool[id(msg)].fl_like == False else False


    @classmethod
    def show_last_message(cls, число):
        if len(cls.msg_pool.values()) < число:
            raise ValueError('число')
        msgs = list(cls.msg_pool.values())[-(число):]
        print(*[x.text for x in msgs])

    @classmethod
    def total_messages(cls):
        return len(cls.msg_pool)


class Message:

    def __init__(self, text: str, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.set_like(msg)
print(Viber.msg_pool)
Viber.remove_message(msg)
Viber.show_last_message(2)

