#Đưa ra một RuntimeError exception.

class RuntimeError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)

try:
    print("And now,....")
    raise RuntimeError('...')
    print('not print')
except RuntimeError as problem:
    print(problem)