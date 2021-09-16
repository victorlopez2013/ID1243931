# ID:1243931 Lopez, Victor A
# define items and take user input the form of a float
L = float(input("Enter amount of lemon juice (in cups):\n"))
W = float(input("Enter amount of water (in cups):\n"))
N = float(input("Enter amount of agave nectar (in cups):\n"))
S = float(input("How many servings does this make?\n"))

print('') # blank spacing between lines

# format is required as well as float use
print("Lemonade ingredients - yields {:.2f} servings".format(S))
print("{:.2f} cup(s) lemon juice".format(L))
print("{:.2f} cup(s) water".format(W))
print("{:.2f} cup(s) agave nectar".format(N))

print('') # blank spacing between lines

# take new input & covert serving input into float servings (cups)

deser = float(input("How many servings would you like to make?\n"))
print('')

# because math and I suck- need to manually calculate desired servings
total = deser / S
D_L1 = (L * total )
D_W1 = (W * total)
D_N1 = (N * total)

print("Lemonade ingredients - yields {:.2f} servings".format(deser))
print("{:.2f} cup(s) lemon juice".format(D_L1))
print("{:.2f} cup(s) water".format(D_W1))
print("{:.2f} cup(s) agave nectar\n".format(D_N1))


# shrinking code is good practice. convert gallons & print (part 3)
print("Lemonade ingredients - yields {:.2f} servings".format(deser))
print("{:.2f} gallon(s) lemon juice".format(L * deser / (S * 16)))
print("{:.2f} gallon(s) water".format(W * deser / (S * 16)))
print("{:.2f} gallon(s) agave nectar".format(N * deser / (S * 16)))