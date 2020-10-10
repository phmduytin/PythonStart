# Viết chương trình tính tần suất các từ từ input.
# Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.
# Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Thì output phải là:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

str = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"

arrStr = sorted(str.split())
n = len(arrStr)

# res = []
#
# i = 1
# count = 1
# while i < n:
#     if arrStr[i] == arrStr[i - 1]:
#         count += 1
#         i += 1
#     else:
#         res.append((arrStr[i - 1], count))
#         count = 1
#         i += 1
#         if i == n:
#             res.append((arrStr[i - 1], 1))
#
# for a in res:
#     print("%s:%d" % (a[0], a[1]))

freq = {}

for word in str.split():
    freq[word] = freq.get(word, 0) + 1

words = sorted(freq.keys())

for w in words:
    print('%s:%d' % (w, freq[w]))
