import random

exit = False
while not exit:
    num = random.randrange(0, 5, 1)
    print("Guess a number between 0-5: ")
    userInput = input()
    if str(num) == str(userInput):
        print("you guessed correctly!")
        exit = True
    else:
        print("your guess was wrong, the answer was " + str(num))
