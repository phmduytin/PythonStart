#Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3 (bao gồm cả hai số)
# và các giá trị bình phương của chúng

def printDict():
    dict = {}
    dict[1] = 1
    dict[2] = 2**2
    dict[3] = 3**2
    print(dict)

printDict()
