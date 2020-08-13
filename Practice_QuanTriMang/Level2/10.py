import math

X = int(input('Nhap X: '))
Y = int(input('Nhap Y: '))

arr = [[0]*Y for _ in range(X)]

#for i in range(X):
#    arr.append([0] * Y)


for i in range(X):
    for j in range(Y):
        arr[i][j] = i * j
        print(arr[i][j], end=' ')
    print()
