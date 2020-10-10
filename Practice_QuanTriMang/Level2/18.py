#Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

#Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

a = int(input('Nhap a: '))

res = 4*a + 3*a*10 + 2*a*100 + a*1000

print(res)
