# Viết một chương trình để tạo tuple khác, chứa các giá trị là
# số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst = [x for x in tup if x % 2 == 0]
tup2 = tuple(lst)
print(tup2)
