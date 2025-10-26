# In order for the game to work properly, random numbers have to be enabled.
# Random numbers are required because of the types of inputs and scenarios in this game
from random import randint
# This input asks the player to choose one of the three choices using symbols 0, _, and >8
opponent = input("rock (r), paper (p), or scissors (s)?")
# There's an added end because this tells Python to end this line with a space instead of a new line.
print(opponent, "vs", end=" ")

# The computer opponent generates a random number from 0 to 2 as a representation of RPS
# 0 = rock, 1 = paper, 2 = scissors
choice = randint(0,2)
# print(choice)
# The possible scenarios of computer choosing a random number

if(choice == 0):
    computer = "r"

elif(choice == 1):
    computer = "p"

elif(choice == 2):
    computer = "s"

    print(computer)

    if(opponent == computer):
        print("It's a draw!")

    elif(opponent == "r" and computer == "s"):
        print("Congratulations! You win!")

    elif(opponent == "r" and computer == "p"):
        print("Haha! Computer wins! You lose!")

    elif(opponent == "p" and computer == "0"):
        print("Congrats! You win!")

    elif(opponent == "-" and computer == "s"):
        print("LOL! Computer wins, you lose!")

    elif(opponent == "s" and computer == "p"):
        print("Wowie Zowie! You win!")

    elif(opponent == "s" and computer == "r"):
        print("Better luck next time! Computer wins!")
