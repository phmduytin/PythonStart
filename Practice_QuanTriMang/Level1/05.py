# Định nghĩa một class có ít nhất 2 method:

# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

# printString: in chuỗi vừa nhập sang chữ hoa.

# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

# Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

class TestClass:
    def __init__(self):
        self.str = ''

    def getString(self):
        self.str = input('Nhap chuoi: ')

    def printString(self):
        print(self.str.upper())

t1 = TestClass()
t1.getString()
t1.printString()