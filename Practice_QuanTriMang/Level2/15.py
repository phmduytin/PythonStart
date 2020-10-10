#Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này)
# sao cho tất cả các chữ số trong số đó là số chẵn.
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

def isEven(x):
    strX = str(x)
    for i in strX:
        if int(i) % 2 != 0:
            return False
    return True


res = []

for i in range(1000, 3001):
    if isEven(i):
        res.append(str(i))

print(','.join(res))
