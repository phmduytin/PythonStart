# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456
import re

input = "ABd1234@1,a F1#,2w3E*,2We3345"

arrPass = input.split(',')

res = []

for pw in arrPass:
    if len(pw) < 6 or len(pw) > 12:
        continue
    else:
        pass

    if not re.search('[a-z]', pw):
        continue
    elif not re.search('[A-Z]', pw):
        continue
    elif not re.search('[$#@]', pw):
        continue
    elif not re.search('[0-9]', pw):
        continue
    else:
        pass

    res.append(pw)

print(','.join(res))
