import random

a = []
n = 10000

for i in range(n):
    x = random.randint(0, 100)
    a.append(x)

print(a)

for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

print(a)
