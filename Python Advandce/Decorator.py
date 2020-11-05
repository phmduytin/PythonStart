# 1.
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operate(func, x):
#     return func(x)
#
# print(operate(inc, 3))

# #2.
# def make_prety(func):
#     def inner():
#         print("I got decorator")
#         func()
#     return inner
#
# @make_prety
# def ordinary():
#     print("I am ordinary")
#
# #ordinary = make_prety(ordinary)
# ordinary()


# 3.
# def smart_divide(func):
#     def inner(a, b):
#         if b == 0:
#             print('Divide zero')
#             return
#         return func(a, b)
#
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     return a / b
#
#
# x = divide(3, 0)
# print(x)

# 4.
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner



@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

