#number guessing game.
import random
#asking user to enter a number till which they wanna guess it, e.g. if user enter 10, the number to be guessed will be from between 0-10.
top_number = input("Type a number: ")
if top_number.isdigit():
    top_number = int(top_number)
#If the user types 0, meaning no number can be generated. so we will ask them to enter number greater than 0
    if top_number <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()
#If user enters something otherthan a no. like 'a' or 'kant', we will ask then to enter a proper number.
else:
    print("please type a number next time. ")
    quit()
#generating a random number from user given range.
random_number = random.randrange(0, top_number)
guess = 0
while True:
    guess += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        #again checking if user enters a number
    else:
        print("please type a number next time. ")
        continue
#if user guessed the no. on first try.
    if user_guess == random_number:
        print("you got it. ")
        break
        #telling user if they are above the number
    elif user_guess > random_number:
        print("You were above the number!")
        #telling user if they are below the number
    else:
        print("You were below the number!")

print("You got it in", guess, "guesses")
