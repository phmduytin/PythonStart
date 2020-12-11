import time
import threading

def print_hello():
    for i in range(3):
        print('Hello')
        time.sleep(1)

def print_hi():
    for i in range(3):
        print('Hi')
        time.sleep((2))

t1 = threading.Thread(target=print_hello)
t2 = threading.Thread(target=print_hi)

t1.start()
t2.start()


