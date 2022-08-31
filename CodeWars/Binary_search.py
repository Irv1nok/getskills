from random import randint
# massive = [randint(1, 100) for _ in range(1, 100)] # генератор массива
massive = [randint(0, 20) for _ in range(10)]
massive.sort()

def bin_search(mas, target):
    start = 0
    end = len(mas) - 1
    mid = len(mas) // 2
    while mas[mid] != target and start <= end:
        if target > mas[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
        print(mid)
    if start > end:
        return None
    else:
        return mid
print(massive)
print(bin_search(massive, 9)) # Возвращает индекс числа в массиве