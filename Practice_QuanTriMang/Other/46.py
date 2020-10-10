# Viết chương trình Python dùng map() để tạo list chứa các giá trị bình phương của
# các số trong [1,2,3,4,5,6,7,8,9,10].

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binhphuong(n):
    return n**2

m = map(binhphuong, lst)

print(list(m))