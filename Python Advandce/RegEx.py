import re

# 1.
# partern = "\d+"
# test_string = 'a12aa foo3 thef32oo'
#
# result = re.findall(partern, test_string)
#
# print(result)

# 2.
# partern = "\d+"
# test_string = 'a12aa foo3 thef32oo'
#
# result = re.split(partern, test_string, 2)
#
# print(result)

# 3.
# partern = "\s+"
# test_string = "tien  123 very \ngood 4"

# re.sub()
# result = re.sub(partern, "...", test_string)

# re.subn()
# result = re.subn(partern, "...", test_string)

# print(result)

# 4.re.search()

partern = "(\d{3}) (\d{2})"

test_string = '39801 356, 2102 1111'
match = re.search(partern, test_string)

if match:
    print(match.group())
else:
    print("Khong khop")

print(match.group(1,2))

print(match.start())
print(match.end())
print(match.span())
print(match.re)
print(match.string)