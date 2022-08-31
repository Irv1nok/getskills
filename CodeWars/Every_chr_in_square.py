def square_digits(num):
    return int(''.join(str(int(x)**2) for x in str(num)))






print(square_digits(9119))