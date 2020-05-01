numberOfPrime = 500
numberPrimeCount = 0
numberPrimeOfLine = 10
primeOfLineCount = 0

i = 2

while numberPrimeCount < numberOfPrime:
    for j in range(2, i // 2):
        if i % j == 0:
            break
    else:
        numberPrimeCount += 1
        primeOfLineCount += 1
        print("%6d" % i, end='')
        if primeOfLineCount == 10:
            primeOfLineCount = 0
            print()
    i+=1
