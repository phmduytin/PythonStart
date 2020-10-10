# Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
# Định dạng nhật ký được hiển thị như sau:

# D 100
# W 200

# (D là tiền gửi, W là tiền rút ra).

# Giả sử đầu vào được cung cấp là:

# D 300
# D 300
# W 200
# D 100
# Thì đầu ra sẽ là:
# 500
res = 0
while True:
    s = input()
    if s == '':
        break
    arrS = s.split(' ')
    if arrS[0] == 'D':
        res += int(arrS[1])
    elif arrS[0] == 'W':
        res -= int(arrS[1])
    else:
        pass

print(res)