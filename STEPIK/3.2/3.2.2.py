from random import randint, choices

# class RandomPassword:
#
#     def __init__(self, psw_chars, min_length, max_length):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):
#         length = randint(self.min_length, self.max_length)
#         return ''.join(choices(self.psw_chars, k=length))
#
#
min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

# rnd = RandomPassword(psw_chars, min_length, max_length)
# lst_pass = [rnd() for _ in range(3)]
# print(lst_pass)

"""ЗАМЫКАНИЕ"""


def Random_password(chars, min, max):
    def innner():
        length = randint(min, max)
        return ''.join(choices(chars, k=length))

    return innner

Random_password = Random_password(psw_chars, min_length, max_length)
password_list = [Random_password() for _ in range(3)]
print(password_list)