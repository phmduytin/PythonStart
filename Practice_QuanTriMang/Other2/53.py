# Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng.
# Class Hinhchunhat có method để tính diện tích.

class Hinhchunhat:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def Area(self):
        return self.w * self.h


hcn = Hinhchunhat(3, 4)
print(hcn.Area())
