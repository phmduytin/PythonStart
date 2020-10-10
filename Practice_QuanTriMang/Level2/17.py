# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

# Giả sử đầu vào là: Quản Trị Mạng

# Thì đầu ra là:

# Chữ hoa: 3

# Chữ thường: 8

# s = input('Nhap dau vao: ')
s = 'Quản Trị Mạng'

count = {'hoa': 0, 'thuong': 0}

for ch in s:
    if ch.islower():
        count['thuong'] += 1
    elif ch.isupper():
        count['hoa'] += 1
    else:
        pass

print('Chữ hoa: {0} \nChữ thường: {1}'.format(count['hoa'], count['thuong']))

