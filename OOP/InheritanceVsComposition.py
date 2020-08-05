class addsub():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y


class muldiv():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

    def div(self):
        if self.y != 0:
            return self.x / self.y


class calc():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.addsub = addsub(x, y)
        self.muldiv = muldiv(x, y)

    def add(self):
        return self.addsub.add()

    def sub(self):
        return self.addsub.sub()

    def mul(self):
        return  self.muldiv.mul()

    def div(self):
        return self.muldiv.div()

    def pow(self):
        return self.x**self.y

cal = calc(10, 5)

print(cal.add(), cal.sub(), cal.mul(), cal.div(), cal.pow())

