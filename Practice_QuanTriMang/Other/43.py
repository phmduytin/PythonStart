# Viết một chương trình để tạo ra và in tuple chứa các số chẵn được
# lấy từ tuple (1,2,3,4,5,6,7,8,9,10).
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

lst2 = [x for x in tup if x % 2 == 0]
print(tuple(lst2))
