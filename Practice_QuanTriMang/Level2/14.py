#Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số,
# phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không.
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

#Ví dụ đầu vào là: 0100,0011,1010,1001

#Đầu ra sẽ là: 1010

res = []

'''def binToNum(x):
    num = 0
    for i in range(0,len(x)):
        num += int(x[-i-1]) * (2**i)
    return num
'''

# arr = input("Nhap day nhi phan: ").split(',')
arr = '0100,0011,1010,1001'.split(',')

for x in arr:
    intX = int(x, 2)
    if intX % 5 == 0:
        res.append(str(x))

print(','.join(res))
