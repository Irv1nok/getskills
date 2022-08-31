def high_and_low(numbers):
    l = list(numbers.split())
    for x in range(len(l)):
        for y in range(len(l) - 1):
            if int(l[y]) > int(l[y + 1]):
                l[y], l[y + 1] = l[y + 1], l[y]

    return f"{l[-1]} {l[0]}"

# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))