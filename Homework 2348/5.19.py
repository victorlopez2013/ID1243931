# ID:1243931 Lopez, Victor A
print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

# prompt user for 2 services
s1 = input("Select first service:\n")
s2 = input("Select second service:\n")

print('')
print("Davy's auto shop invoice")
print('')
serviceDic = {'Oil change':35, 'Tire rotation':19, 'Car wash':7, 'Car wax':12, '-':0}
# now for the loop
if s1 =='Oil change':
    print('Service 1: Oil change, $35')
elif s1 =='Tire rotation':
    print('Service 1: Tire rotation, $19')
elif s1 =='Car wash':
    print('Service 1: Car wash, $7')
elif s1 =='Car wax':
    print('Service 1: Car wax, $12')
else:
    print('Service 1: No service')

if s2 =='Oil change':
    print('Service 2: Oil change, $35')
elif s2 =='Tire rotation':
    print('Service 2: Tire rotation, $19')
elif s2 =='Car wash':
    print('Service 2: Car wash, $7')
elif s2 =='Car wax':
    print('Service 2: Car wax, $12')
else:
    print('Service 2: No service')
print('')
print('Total: ${}'.format(serviceDic[s1] + serviceDic[s2]))
