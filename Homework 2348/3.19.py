# ID:1243931 Lopez, Victor A
# involves more math & math import is glitching
# make a dictionary of given colors with prices from part 4
paint_colors = {'red':35, 'blue':35, 'green':23}
# prompt user to give dimensions
w_h = int(input('Enter Wall Height (feet):\n'))
w_w = int(input('Enter Wall With (feet):\n'))
a = w_h * w_w
print('Wall area:{} square feet.'.format(a))
# using % is not easy but here goes
p_n = a/350
# 350 is num of sq ft per can. reduced code
print('Paint needed: %f gallons' %p_n)
print('Cans needed: {} can(s)'.format(round(p_n)))
color = input('Choose a color to pain the wall:\n')
print("Cost of purchasing",color,":${}".format(paint_colors[color]))
