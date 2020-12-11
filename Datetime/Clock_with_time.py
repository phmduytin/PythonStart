import time
import os

while True:
    curent_time = time.localtime()
    res = time.strftime("%H:%M:%S %p", curent_time)
    print(res)
    time.sleep(1)
    os.system('cls')

