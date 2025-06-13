from random import randint

for i in range(1,6):
    guessNumber = int(input("Guess a random number between 1 to 5 : "))
    randomNumber = randint(1,5)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was", randomNumber)