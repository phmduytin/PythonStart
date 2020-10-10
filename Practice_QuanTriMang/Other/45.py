# Viết chương trình Python có thể lọc các số chẵn trong danh sách sử dụng hàm filter.
# Danh sách là [1,2,3,4,5,6,7,8,9,10].

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = filter(lambda x: x % 2 == 0, lst)
print(list(res))
