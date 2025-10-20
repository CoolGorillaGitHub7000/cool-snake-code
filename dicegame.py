import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2 
# When the two dice equal 7 or 11, that's a win. 1+6, 2+5, 3+4, and 5+6
if (total==7 or total==11):
    print ("You're Winner!")
elif (die1==die2):
    if (die1==6 and die2==6):
        print ("Jackpot! You get no money! Just bragging rights.")
    else:
        print ("Doubles! You're double winner!")
else:
    print ("You're loser!")