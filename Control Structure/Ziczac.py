numLine = int(input("Input number line ziczac: "))
numPointOfLine = int(input("Input number point a line: "))

m = numPointOfLine
n = (m - 1) * numLine + 1

arr = [[0] * n for _ in range(m)]
arr[m - 1][0] = 1

x = m - 1
y = 0
forward = True

while True:
    y += 1
    if y >= n:
        break

    if forward:
        if x == 0:
            forward = False
            y -= 1
            continue
        x -= 1

    else:
        if x == m - 1:
            forward = True
            y -= 1
            continue
        x += 1

    arr[x][y] = 1

for i in range(0, m):
    for j in range(0, n):
        if arr[i][j] == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
