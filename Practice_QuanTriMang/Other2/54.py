# Định nghĩa một class có tên là Shape và class con là Square.
# Square có hàm init để lấy đối số là chiều dài.
# Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.

class Shape:
    def __init__(self):
        pass
    def Area(self):
        return 0


class Square(Shape):
    def __init__(self, d):
        Shape.__init__(self)
        self.dai = d

    def Area(self):
        return self.dai ** 2

vuong = Square(2)
print(vuong.Area())
