import random
import time
time_start = time.perf_counter()
a = []
n = 200

for i in range(n):
    a.append(random.randint(0, 100))

print(a)

for i in range(1, n):
    j = i
    while j > 0:
        if a[j] < a[j - 1]:
            tmp = a[j]
            a[j] = a[j - 1]
            a[j - 1] = tmp
            j = j - 1
        else:
            break

print(a)

time_stop = time.perf_counter()

print(time_stop - time_start)