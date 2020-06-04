'''
    S = 1 + 2 + 3 + 4 + ..... + n
'''


def SumOfN(n):
    if n == 1:
        return 1
    return n + SumOfN(n - 1)


print(SumOfN(10))

'''
    str = 'aabbbbbccc' => 'abc'
'''

str = 'aabbbbcccccc'


# def reduce_str(s, i, n):
#     if i == n - 1:
#         return s[i]
#     if s[i] == s[i + 1]:
#         return reduce_str(s, i + 1, n)
#     return s[i] + reduce_str(s, i + 1, n)

def reduce_str(str):
    if len(str) == 1:
        return str
    if str[0] == str[1]:
        return reduce_str(str[1:])
    return str[0] + reduce_str(str[1:])


res = reduce_str(str)

print(res)
