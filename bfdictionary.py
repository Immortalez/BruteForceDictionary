from math import factorial

# Taking necessary information form a user
min_length = input("Minimal length: ")
max_length = input("Maximal length: ")
characters = "aaabbcccccdefghijklmnopqrstuwxyz"  # String with all the characters to be used
# characters = "aaabbcccccdefghijklmnopqrstuwxyz"  # String with all the characters to be used

# Eliminating duplicates
char_set = sorted(list(set(characters)))

combinations = len(characters) ** 5  # Stores the amount of possible combinations
print("Possible combinations: {}".format(combinations))


