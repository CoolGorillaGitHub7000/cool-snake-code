# These are my favorite hockey players. (Definitely not biased)
hockeyplayers = ["Sidney Crosby", "Evgeni Malkin", "Kris Letang"]
print(hockeyplayers[1])

# This for loop loops a print of a sentence along with the defined list after on repeat until the list ends.
for hockeyplayer in hockeyplayers:
    print("Because he plays for the Pittsburgh Penguins and has been highly dominant, I love", hockeyplayer)

# Here is code that reverses the order of the list. It uses a negative number starting at -1 (Kris Letang) and lists backwards
print(hockeyplayers[-3])

# Now what happens if I choose number 3 or more, or a negative number below -3?
print(hockeyplayers[-5])
# The code gives an error that the input is out of range
# What about a negative? Same thing.

# Let's replace an item on the list shall we?
hockeyplayers[2] = "Bryan Rust"
print(hockeyplayers)