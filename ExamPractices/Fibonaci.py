def Fib(n: int):
    print
    if n <= 2:
        return 1
    return Fib(n - 1) + Fib(n - 2)

print(Fib(10))