# ID:1243931 Lopez, Victor A
# User input 1
userNum = int(input("Enter an integer:\n"))
# output set integer
print(userNum)
print("You Entered:{}".format(userNum))
# square user integer
# {} is used a place holder for numeric values
# format allows for inline operation. number, operation for number
print("{} squared is {}".format(userNum, userNum**2))
# new number
userNum2 = int(input("Enter another Integer:\n"))
# follow by 2 operations: addition and multiplication - modify line 9 {userNum} + {userNum2} is {operation result} and so on.
print("{} + {} is {}".format(userNum, userNum2, userNum + userNum2))
print("{} * {} is {}".format(userNum, userNum2, userNum * userNum2))
