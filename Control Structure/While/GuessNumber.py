numberCorrect = 82

while True:
    number = int(input("Guess a number between 0 and 100: "))

    if number > numberCorrect:
        print("The correct number is less than your number input ", number)
    elif number < numberCorrect:
        print("The correct number is more than your number input ", number)
    else:
        print("Correct!!!")

