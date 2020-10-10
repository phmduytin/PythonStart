class DaGiac:

    def __init__(self, socanh):
        self.n = socanh
        self.canh = [0 for i in range(socanh)]

    def nhapcanh(self):
        self.canh = [float(input('Nhap gia tri canh thu {}: '.format(i + 1))) for i in range(self.n)]

    def hienthicanh(self):
        for i in range(self.n):
            print("Giá trị cạnh", i + 1, "là", self.canh[i])


class TamGiac(DaGiac):
    def __init__(self):
        DaGiac.__init__(self, 3)

    def Area(self):
        a, b, c = self.canh
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b)*(s - c))**0.5
        print(area)

tg = TamGiac()
tg.nhapcanh()
tg.hienthicanh()
tg.Area()