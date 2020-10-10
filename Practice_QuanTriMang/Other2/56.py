# Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.

def calc():
    return 5 / 0


try:
    print(calc())
except ZeroDivisionError:
    print('Chia cho một số 0')
except Exception as problem:
    print(problem)
finally:
    print('Phép tính bị huỷ')
