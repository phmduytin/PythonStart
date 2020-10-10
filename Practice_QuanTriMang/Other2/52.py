# Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính.
# Circle có một method có thể tính diện tích.
import math


class Circle:
    def __init__(self, r):
        self.r = r

    def calcArea(self):
        return math.pi * self.r ** 2

tron = Circle(3)
print(tron.calcArea())

