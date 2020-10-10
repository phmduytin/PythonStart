# Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng,
# in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No".

str = input()
if str == 'yes' or str == 'YES' or str == 'Yes':
    print('Yes')
else:
    print('No')
