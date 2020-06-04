import functools

square = lambda x: x ** 2

print(list(map(square, [1, 2, 3])))

num = [1, 4, 45, 4, 65, 65, 0, 7, 9, 6, 67, 69, 69, 98]

print(list(filter(lambda x: x % 3 == 0, num)))

print(sum(num))

print(functools.reduce(lambda x, y: x + y, num))

fact = lambda x: x * fact(x - 1) if x > 1 else 1

print(fact(3))

def edit_word(words, func):
    for word in words:
        yield func(word)

res = edit_word(['hello', 'word'], lambda x: x.upper())

print(list(res))
