# Định nghĩa một hàm có thể tạo dictionary, chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20)
# và các giá trị bình phương của chúng. Hàm chỉ in các giá trị mà thôi.
def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2

    for v in d.values():
        print(v)


printDict()
