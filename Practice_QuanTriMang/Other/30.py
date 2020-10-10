# Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn
# trong giao diện điều khiển.
# Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.

def compareString(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        print(s1)
    elif l1 < l2:
        print(s2)
    else:
        print(s1)
        print(s2)


compareString('1234', '123')
