number = int(input("Input odd number: "))
while number % 2 == 0:
    print("Sorry, please input odd number!")
    number = int(input("Input odd number: "))

for i in range(number, -1, -2):
    j = 0
    n = (number-i)//2
    while j < number:
        if j < n or j >= number - n:
            print(' ', end='')
        else:
            print(i, end='')
        j += 1
    print()
