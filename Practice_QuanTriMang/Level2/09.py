# Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H])
# (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
# Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến,
# được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.

# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

import math


def calc(C, D, H):
    res = math.sqrt((2 * C * float(D)) / H)
    return str(round(res))


arr = input('Nhap chuoi D: ').split(',')

res = list()

for i in arr:
    res.append(calc(50, int(i), 30))

print(','.join(res))
