# In order for the game to work properly, random numbers have to be enabled.
# Random numbers are required because of the types of inputs and scenarios in this game
from random import randint
# This input asks the player to choose one of the three choices using symbols 0, _, and >8
opponent = input("rock (0), paper (_), or scissors (>8)?")

print(opponent, "vs")