#Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

#Thì đầu ra sẽ là:

#Số chữ cái là: 10
#Số chữ số là: 3

s = 'hello world! 123'

countNum = 0
countStr = 0

for i in s:
    if i.isdigit():
        countNum += 1
    elif i.isalpha():
        countStr += 1

print('Số chữ cái là: ', countStr)
print('Số chữ số là: ', countNum)
