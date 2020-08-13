#Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng,
# loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.

#Giả sử đầu vào là: hello world and practice makes perfect and hello world again

#Thì đầu ra là: again and hello makes perfect practice world

items = 'hello world and practice makes perfect and hello world again'.split(' ')

#res = []
#for item in items:
#    if res.__contains__(item) == False:
#        res.append(item)

res = list(set(items))
res.sort()

print(' '.join(res))