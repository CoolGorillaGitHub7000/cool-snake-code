# import random
die1 = 3
die2 = 6
total = die1 + die2 
# When the two dice equal 7 or 11, that's a win. 1+6, 2+5, 3+4, and 5+6
if (total==7 or total==11):
    print ("You're Winner!")
# When the dice equal one another, this is considered a doubles win. If they both equal 6, it's a jackpot.
elif (die1==die2):
    if (die1==6 and die2==6):
        print ("Jackpot! You get no money! Just bragging rights.")
    else:
        print ("Doubles! You're double winner!")
# If the dice aren't double, or equaled to 7/11, the player loses
else:
    print ("You're loser!")