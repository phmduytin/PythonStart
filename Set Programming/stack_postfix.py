equal = '20+3*4-(5+2)/7'
stack = []
postfix = []
infix = []
num = ''
cnt = 0
while cnt < len(equal):
    if '0' <= equal[cnt] <= '9':
        num += equal[cnt]
        if cnt == len(equal)-1:
            infix.append(num)
            break
    else:
        if num != '':
            infix.append(num)
        num = ''
        infix.append(equal[cnt])
    cnt += 1

for x in infix:
    if x == ')':
        postfix.append(stack.pop())
    elif x.isdigit():
        postfix.append(x)
        if len(stack) != 0 and stack[len(stack) - 1] != '+' and stack[len(stack) - 1] != '-' and len(postfix) > 2:
            postfix.append(stack.pop())

    elif x == '(' or x == ' ':
        continue
    else:
        stack.append(x)

while True:
    if len(stack) == 0:
        break
    postfix.append(stack.pop())

res = 0.0

print(postfix)

for x in postfix:
    if x.isdigit():
        stack.append(x)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if x == '*':
            res = a * b
            stack.append(res)
        elif x == '/':
            res = a / b
            stack.append(res)
        elif x == '+':
            res = a + b
            stack.append(res)
        elif x == '-':
            res = a - b
            stack.append(res)

print(stack.pop())
