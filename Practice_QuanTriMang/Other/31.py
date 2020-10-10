# Định nghĩa hàm có thể chấp nhận input là số nguyên và
# in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
def checkValue(n):
    if n % 2 == 0:
        print("Đây là số chẵn")
    else:
        print("Đây là số lẻ")

checkValue(7)