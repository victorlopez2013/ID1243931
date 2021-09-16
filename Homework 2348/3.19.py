import math

# ID:1243931 Lopez, Victor A
# involves more math & math import is glitching
# make a dictionary of given colors with prices from part 4

paint_colors = {'red':35, 'blue':75, 'green':23}
# prompt user to give dimensions
w_h = int(input('Enter wall height (feet):\n'))
w_w = int(input('Enter wall width (feet):\n'))
a = w_h * w_w
print('Wall area: {} square feet'.format(a))

# using % is not easy but here goes
p_n = a/350

# 350 is num of sq ft per can. reduced code
print('Paint needed: {:.2f} gallons'.format(p_n))
print('Cans needed: {} can(s)'.format(round(p_n)))
print('')
color = input('Choose a color to paint the wall:\n')
print("Cost of purchasing", color, "paint: ${}".format(paint_colors[color]))
