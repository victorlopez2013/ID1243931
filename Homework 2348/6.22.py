''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

solution = False
for x in range(-10, 11):
    for y in range(-10, 11):
        equation1 = a * x + b * y
        equation2 = d * x + e * y
        if equation1 == c and equation2 == f:
            print( x, y)
            solution = True

if solution == False:
    print("No solution")
