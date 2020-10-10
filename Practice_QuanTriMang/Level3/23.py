#Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7

def putNumber(n):
    for i in range(0, n+1):
        if i%7==0:
            yield i

print(list(putNumber(22)))
