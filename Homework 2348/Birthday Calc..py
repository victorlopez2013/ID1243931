from datetime import date
def calculateAge(currentdate,birthdate):
    today = currentdate
    age = today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,))
    return age
print('Welcome to birthday calculator')
print('Please enter the current date by year, month & day')
y = int(input("Year:"))
m = int(input("Month:"))
d = int(input("Day:"))
print('Enter your birthday:')
y1 = int(input("Year:"))
m1 = int(input("Month:"))
d1 = int(input("Day:"))
print("Year:, y1 ")
print("Month:, m1 ")
print("Day:, d1 ")
print("you are", calculateAge(date(y,m,d),date(y1, m1, d1)),"years old.")
if date == (m1, d1):
    print('Happy Birthday')