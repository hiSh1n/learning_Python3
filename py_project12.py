#A simple quiz game.
#we'll ask users some questions, calculate their score based on the answer and then give the result output.
print("WELCOME TO THE QUIZ !")

#asking user if they wanna play or not

wanna_play = input("Do you wanna play? yes/no ").lower()

#if they say "yes" then continue otherwise quit.

if  wanna_play != "yes":
    quit()

print("Let's play :)")

score = 0

answer = input("What is the full form of CPU? ").lower()

if answer == "central processing unit":
    print("Correct ! +1 point")
    score += 1
else:
    print("! incorrect no points for you")

answer = input("What does RAM stands from? ").lower()

if answer == "random access memory":
    print("Correct ! +1 point")
    score += 1
else:
    print("! incorrect no points for you")

print("You got " + str(score) + " points !")
print("You got " + str((score / 2) * 100) + " %")
