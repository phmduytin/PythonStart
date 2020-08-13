# Viết một chương trình có thể tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

res = 1

n = int(input('Nhap so cho truoc: '))

# for i in range(1, n + 1):
#    res *= i

def gt(x):
    if x == 1:
        return x
    return x * gt(x - 1)

res = gt(n)

print(res)
