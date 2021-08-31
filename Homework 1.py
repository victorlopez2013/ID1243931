#homework 1
print("Hello, and welcome to Birthday Calculator")
print("Please enter current date by year, month, day & then input date of birth in the same order")
y = int(input("Year:"))
m = int(input("Month:"))
d = int(input("Day:"))
print("Year:", y)
print("Month:", m)
print("Day:", d)
print("Birthdate")
y1 = int(input("Year:"))
m1 = int(input("Month:"))
d1 = int(input("Day:"))
print("Year:", y1)
print("Month:", m1)
print("Day:", d1)
if m<m1:
    age_year = y-y1-1
elif m == m1:
     if d<d1:
         age_year = y - y1-1
     elif d==d1:
          age_year = y -y1
          print("Happy Birthday!")
     else:
          age_year = y-y1
else:
      age_year = y-y1
print("Your age is:", age_year)