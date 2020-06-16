import functools

Fib = lambda x: Fib(x - 1) + Fib(x - 2) if x > 2 else 1

print(Fib(10))

Foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

num = filter(lambda x: x % 2 == 1, Foo)

print(functools.reduce(lambda x, y: x + y, num))
