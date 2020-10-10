#Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com,
# hãy viết một chương trình để in username của địa chỉ email cụ thể.
# Cả username và companyname chỉ bao gồm chữ cái.

#Ví dụ: Nếu cung cấp địa chỉ email QTM@quantrimang.com thì đầu ra sẽ là: QTM.

import re

email = "QTM@quantrimang.com"
arrS = email.split('@')
print(arrS[0])

