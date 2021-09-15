# ID:1243931 Lopez, Victor A
# define items and take user input the form of a float
L = float(input("Enter the amount of Lemon Juice (in cups):\n"))
W = float(input("Enter the amount of Water Juice (in cups):\n"))
N = float(input("Enter the amount of Agave Juice (in cups):\n"))
S = float(input("How many servings does this make?:\n"))

# format is required as well as float use
print("Lemonade Ingredients -yield {0:.2f} servings".format(S))
print("{:.2f} cup(s) of lemon juice".format(L))
print("{:.2f} cup(s) of Water".format(W))
print("{:.2f} cup(s) of".format(N))

# take new input & covert serving input into float servings (cups)
D_S = float(input("How many servings would you like?:\n"))
# because math and I suck- need to manually calculate desired servings
D_L1 = (L * D_S / S)
D_W1 = (W * D_S / S)
D_N1 = (N * D_S / S)
print("Lemonade ingredients yield - {:.2}".format(S))
print("{:.2f} cup(s) of lemon juice".format(D_L1))
print("{:.2f} cup(s) of Water".format(D_W1))
print("{:.2f} cup(s) of Agave".format(D_N1))
print("\n")
# shrinking code is good practice. convert gallons & print (part 3)
print("Lemonade ingredients yield - {:.2}".format(S))
print("{:.2f} gallon(s) of lemon juice".format(L * D_S / (S * 16)))
print("{:.2f} gallon(s) of Water".format(W * D_S / (S * 16)))
print("{:.2f} gallon(s) of Agave".format(N * D_S / (S * 16)))

