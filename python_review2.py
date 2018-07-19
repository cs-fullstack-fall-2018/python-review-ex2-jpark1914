#====Phase 1=====
import random
randomNumber = random.randint(0,10)

#====Phase 2=====

guessedNum = int(input("Guess a number between 0 - 10"))
print("First guess is always wrong try again")

#====Phase 3=====

while(guessedNum != randomNumber  and guessedNum != 'q'):
    guessedNum = int(input(""))
    if(guessedNum == randomNumber):
        print("THAT IS A CORRECT GUESS")
        break
    elif(guessedNum < randomNumber):
        print("Guess a little higher Or press 'q' to quit.")
    elif(guessedNum > randomNumber):
        print("Aim lower or press 'q' to quit.")
    else:
        print("Tis an error, try a different number")
        continue