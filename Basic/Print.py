name = "Tien"
age = 24

print("My name is %s. I am %d" % (name, age))

primeNum = [1, 2, 3, 5, 7, 11, 13, 17, 19]
i = 0

for prime in primeNum:
    print("%2d:  %2d" % (i, prime))
    i += 1

for prime in primeNum:
    print("%3d," % prime, end='')

for x in range(1, 5):
    print('{0:1d} {1:2d} {2:3d}'.format(x, x * x, x * x * x))

print("My name is {name}. I am {age}".format(name="phmduytin", age="24"))
