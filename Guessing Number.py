import random

Num = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print('Please enter a valid integer!')
        continue
    if guess < Num:
        print("Too low!")
    elif guess > Num:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break


#THING I LEARNED 
# USING TRY AND EXCEPT TO HANDLE ERRORS IN CASE THE USER ENTERS A STRING INSTEAD OF AN INTEGER.