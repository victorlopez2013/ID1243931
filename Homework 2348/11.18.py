#Victor Lopez
#PSID: 1243931

numlist = input().split()
poslist = []

for x in numlist:
    if int(x)>=0:
        poslist.append(int(x))
poslist.sort()
for x in poslist:
    print (x, end=" ")