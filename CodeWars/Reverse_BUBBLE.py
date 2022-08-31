def descending_order(num: int):
    l = list(str(num))
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    convert = int(''.join(l))
    return convert


if __name__ == '__main__':
    print(descending_order(485312452))
