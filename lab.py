# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix
# On line 4, there's a double quote ("") missing
print("Welcome to the Debugging Lab!")

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")
# 88 was not an integer. It was in quotes.
scores = [85, 90, 78, 88, 92]
# Colon was missing from score
total = 0
 for total in scores:
    total = total + score

average = total / len(scores)
print("Your average score is:" {average})

highest = 0
for s in scores:
    if s > highest:
        highest = s

print("Your highest score was:" + highest)