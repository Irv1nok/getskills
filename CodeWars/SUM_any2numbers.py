x = [1, 3, 5, 6, 2, 4]
y = 9
for i in range(len(x) - 1):
    for j in range(i + 1, len(x)):
        if x[i] + x[j] == y:
            print(x[i], x[j])


