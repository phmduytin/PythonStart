# Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 đến 20
# (bao gồm cả 1 và 20). Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.
def printList():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst[5:])

printList()