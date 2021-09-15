# Bug here; space issue, 2 lines of code as 1 = error
userNum = int(input())
# squaring needs multiplication
userNumSquared = userNum * userNum
# Output formatting issue here; needs new line
print(userNumSquared, end='\n ')
