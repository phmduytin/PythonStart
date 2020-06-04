def Add(x, y):
    return x + y


def addInt(x: int, y: int) -> int:
    return x + y


def AddABCXYZ(*y):
    return sum(y)


# print(AddABCXYZ(1, 5, 6, 7, 4, 3))

def a(head, *middle, tail):
    print(head**2)
    for i in middle:
        print(i)


a(10, 4, 5, 6, tail=8)

