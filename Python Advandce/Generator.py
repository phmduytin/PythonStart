# def Init(n):
#     for i in range(0,n):
#         if i%2==0:
#             yield i
#
# lst = Init(10)
#
# print(list(lst))

#Dao chuoi
# def rev_str(str):
#     n = len(str)
#     for i in range(n-1,-1,-1):
#         yield str[i]
#
# print(''.join(list(rev_str('abcdef'))))

#Bieuthuc
lst = [1,2,3,4]

print(sum(x for x in lst))
