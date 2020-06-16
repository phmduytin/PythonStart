import random

a = []
n = 10

for i in range(n):
    a.append(random.randint(0, 100))

print(a)

for i in range(n - 1):
    i_min = i
    for j in range(i + 1, n):
        if a[i_min] > a[j]:
            i_min = j
    tmp = a[i]
    a[i] = a[i_min]
    a[i_min] = tmp

print(a)
